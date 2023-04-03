from websocket import WebSocketApp, enableTrace
from threading import Thread


class Socket:
	def __init__(self, headers, debug: bool = False, sock_trace: bool = False):
		self.socket_url = "wss://gateway.discord.gg"
		self.socket = None
		self.debug=debug
		self.headers = headers
		enableTrace(sock_trace)



	def connect(self):
		try:
			if self.debug:
				print(f"[socket][start] Starting Socket")

			self.socket = WebSocketApp(
				f"{self.socket_url}/?encoding=json&v=9&compress=zlib-stream",
				header = self.headers(),
				on_message=self.resolve
			)
			self.socket_thread = Thread(target=self.socket.run_forever)
			self.socket_thread.start()

			if self.debug:
				print(f"[socket][start] Socket Started")
		except Exception as e:
			if self.debug:
				print(f"[socket][start] Error while starting Socket : {e}")


	def disconnect(self):
		if self.debug:
			print(f"[socket][close] Closing Socket")
		try:
			self.socket.close()
			self.socket_thread = None
			if self.debug:
				print(f"[socket][close] Socket closed")
		except Exception as e:
			if self.debug:
				print(f"[socket][close] Error while closing Socket : {e}")
		return


	def resolve(self, ws, data):
		try:
			#data = loads(data)
			print(data)
		except Exception as e:
			print(f"[socket][resolve] Error while resolve data : {e}")