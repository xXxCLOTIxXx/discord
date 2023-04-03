from .exceptions import *

from requests import Session
from aiohttp import ClientSession
from json import dumps

class Requester:
	def __init__(self):
		self.web_api = "https://discord.com/api/v9"
		self.session = Session()
		self.token = None

	def headers(self):
		headers = {
			"content-type": "application/json",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
		}
		if self.token:headers["authorization"] = self.token

		return headers


	def make_request(self, method: str, endpoint: str, body: dict = None, allowed_code: int = 200, proxies: dict = None):

		response = self.session.request(method, f"{self.web_api}{endpoint}", data=dumps(body) if body else None, headers=self.headers(), proxies=proxies)
		return checkException(response.text) if response.status_code != allowed_code else response


	async def make_async_request(self, method: str, endpoint: str, body: dict = None, allowed_code: int = 200):
		async with ClientSession() as asyncSession:
			response = await asyncSession.request(method, f"{self.web_api}{endpoint}", data=dumps(body) if body else None, headers=self.headers())
			return checkException(await response.text()) if response.status != allowed_code else response