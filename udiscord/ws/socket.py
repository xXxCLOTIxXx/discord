from websocket import WebSocketApp, enableTrace
from threading import Thread
from time import sleep
from ujson import dumps, loads

from ..utils.requester import Requester
from .. import log
from .socket_handler import Handler
from traceback import print_exc

class Socket(Handler):
	heartbeat_started: bool = False
	req: Requester
	active: bool = False
	heartbeat_interval: int = None

	def __init__(self, sock_trace: bool = False):
		self.socket_url = "wss://gateway.discord.gg"
		self.socket = None
		enableTrace(sock_trace)
		Handler.__init__(self)

	def connect(self):
		try:
			if self.active: return
			log.debug(f"[socket][start] Starting Socket")

			self.socket = WebSocketApp(
				f"{self.socket_url}/?encoding=json&v=9",
				header = self.req.headers(),
				on_message=self.resolve
			)
			self.socket_thread = Thread(target=self.socket.run_forever)
			self.socket_thread.start()
			Thread(target=self.start_heartbeat).start()
			self.active=True
			log.debug(f"[socket][start] Socket Started")
		except Exception as e:
			log.error(f"[socket][start] Error while starting Socket : {e}")


	def disconnect(self):
		if not self.active:return
		log.debug(f"[socket][close] Closing Socket")
		try:
			self.socket.close()
			self.socket_thread = None
			self.active = False
			log.debug(f"[socket][close] Socket closed")
		except Exception as e:
			log.error(f"[socket][close] Error while closing Socket : {e}")


	def resolve(self, ws, data):
		try:
			data = loads(data)
			if data.get("op") == 10:
				self.heartbeat_interval = data['d']['heartbeat_interval'] / 1000
				return
			self.handle_data(data)
		except Exception as e:
			log.warning(f"[socket][resolve] Error while resolve data : {e}")
			print_exc()


	def start_heartbeat(self):
		sleep(0.5)
		identify_payload = {
			"op": 2,
			"d": {
				"token": self.req.token,
				"properties": {
					"os": "Windows",
					"browser": "Firefox",
					"device": ""
				}
			}
		}
		try:self.send(identify_payload)
		except Exception as e:log.critical("[socket][start] Failed connect to discord socket")

		while True:
			if not self.heartbeat_interval: continue
			sleep(self.heartbeat_interval)
			if not self.active:return
			self.send({"op": 1, "d": None})

	def send(self, data: str | dict | bytes):
		if not self.active or not self.socket: return
		log.debug(f"[socket][send]: {data}")
		data = data if isinstance(data, bytes) else dumps(data)
		self.socket.send(data)