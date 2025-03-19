from websocket import WebSocketApp, enableTrace
from threading import Thread
from time import sleep
from ujson import dumps, loads
from random import randrange

from ..utils.requester import Requester
from .. import log
from .socket_handler import Handler
from .. import OPCODE, exceptions, AccountInfo

from traceback import format_exc

class Socket(Handler):
	heartbeat_started: bool = False
	req: Requester
	token: str
	account: AccountInfo
	active: bool = False
	heartbeat_interval: int = None
	sequence: int = 0

	def __init__(self, os: str, browser: str, device: str, sock_trace: bool = False, detailed_error: bool = False, auto_reconnect: bool = True):
		self.auto_reconnect=auto_reconnect
		self.socket_url = "wss://gateway.discord.gg"
		self.socket = None
		self.detailed_error = detailed_error
		enableTrace(sock_trace)
		self.os, self.browser, self.device = os, browser, device
		Handler.__init__(self)

	def connect(self):
		try:
			if self.active: return
			log.debug(f"[socket][start] Starting Socket")

			self.socket = WebSocketApp(
				f"{self.socket_url}/?encoding=json&v=9",
				header = self.req.headers(),
				on_message=self.resolve,
				on_close=self.__on_close,
				on_error=self.__on_error
			)
			self.socket_thread = Thread(target=self.socket.run_forever)
			self.socket_thread.start()
			Thread(target=self.start_heartbeat).start()
			self.active=True
			log.debug(f"[socket][start] Socket Started")
		except Exception as e:
			log.error(f"[socket][start] Error while starting Socket : {e}{'' if not self.detailed_error else f'\n{format_exc()}'}")


	def disconnect(self):
		if not self.active:return
		log.debug(f"[socket][close] Closing Socket")
		try:
			self.socket.close()
			self.socket_thread = None
			self.active = False
			log.debug(f"[socket][close] Socket closed")
		except Exception as e:
			log.error(f"[socket][close] Error while closing Socket : {e}{'' if not self.detailed_error else f'\n{format_exc()}'}")



	def reconnect(self):
		log.debug(f"[socket][reconnect] Reconnecting...")
		self.send({"op": OPCODE.RESUME, "d": {"token": self.token, "session_id": self.account.session_id, "seq": self.sequence-1 if self.sequence>0 else self.sequence}})


	def __on_close(self, close_code, close_msg):
		self.active = False
		if close_code or close_msg:
			log.debug(f"[socket][close][<code {close_code}>]: {close_msg}")
		log.debug(f"[socket][close] Socket closed")


	def __on_error(self, error):
		log.error(f"[socket][error] {error}")

	def resolve(self, ws, data):
		try:
			data = loads(data)
			_op = data.get("op")
			if _op != OPCODE.HEARTBEAT_ACK:
				self.sequence += 1
			if _op == OPCODE.HELLO:
				self.heartbeat_interval = data['d']['heartbeat_interval'] / 1000
				return
			elif _op == OPCODE.HEARTBEAT:
				self.send({"op": OPCODE.HEARTBEAT,"d": self.sequence})
			elif _op == OPCODE.INVALID_SESSION:
				self.disconnect()
				self.sequence = 0
				raise exceptions.InvalidSession("Invalid Session Error.")
			elif _op == OPCODE.RECONNECT:
				self.disconnect()
				if self.auto_reconnect:
					sleep(randrange(1,6))
					self.reconnect()
				else:raise exceptions.NeedToReconnect("Socket reconnection required.")
			else:
				self.handle_data(data)
		except Exception as e:
			log.warning(f"[socket][resolve] Error while resolve data : {e}{'' if not self.detailed_error else f'\n{format_exc()}'}")


	def start_heartbeat(self):
		sleep(0.5)
		identify_payload = {
			"op": OPCODE.IDENTIFY,
			"d": {
				"token": self.req.token,
				"properties": {
					"os": self.os,
					"browser": self.browser,
					"device": self.device,

				},
				"presence": {
					"status": "online",
					"since": 0,
					"activities": [],
					"afk": False
				},
				"compress": False,
				"client_state": {
					"guild_hashes": {},
					"highest_last_message_id": "0",
					"read_state_version": 0,
					"user_guild_settings_version": -1,
					"user_settings_version": -1
				}
			}
		}
		for i in range(5):
			try:
				self.send(identify_payload)
				self.send({"op": OPCODE.VOICE_STATE_UPDATE, "d": {"guild_id": None, "channel_id": None, "self_mute": True, "self_deaf": False, "self_video": False}})
				break
			except Exception as e:
				log.error("[socket][start] Failed connect to discord socket. reconnecting...")
				sleep(1.5)
		else:
			log.critical("[socket][start] Failed connect to discord socket.")

		while True:
			if not self.heartbeat_interval: continue
			sleep(self.heartbeat_interval)
			if not self.active:return
			self.send({"op": 1, "d": self.sequence})

	def send(self, data: str | dict | bytes):
		if not self.active or not self.socket:
			log.debug(f"[socket][send][error]: socket is disabled or not running.")
			return
		log.debug(f"[socket][send]: {data}")
		data = data if isinstance(data, bytes) else dumps(data)
		self.socket.send(data)