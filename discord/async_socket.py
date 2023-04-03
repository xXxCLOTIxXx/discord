from aiohttp import ClientSession
from asyncio import create_task


class AsyncSocket:
	def __init__(self, headers, debug: bool = False):
		self.socket_url = "wss://gateway.discord.gg"
		self.debug=debug
		self.headers = headers

		self.task_resolve = None
		self.socket = None
		self.connection = None

	async def connect(self):
		try:
			if self.debug:
				print(f"[socket][start] Starting Socket")
			self.socket = ClientSession(base_url=self.socket_url)
			self.connection = await self.socket.ws_connect("/?encoding=json&v=9&compress=zlib-stream",headers=self.headers())
			self.task_resolve = create_task(self.resolve())
			if self.debug:
				print(f"[socket][start] Socket Started")
		except Exception as e:
			if self.debug:
				print(f"[socket][start] Error while starting Socket : {e}")


	async def disconnect(self):
		if self.debug:
			print(f"[socket][close] Closing Socket")
		try:
			if self.task_resolve: self.task_resolve.cancel()
			if self.connection:
				await self.connection.close()
				self.connection = None
			if self.socket:
				await self.socket.close()
				self.socket = None
			if self.debug:
				print(f"[socket][close] Socket closed")
		except Exception as e:
			if self.debug:
				print(f"[socket][close] Error while closing Socket : {e}")


	async def resolve(self):
		while True:
			msg = await self.connection.receive()
			print(msg)