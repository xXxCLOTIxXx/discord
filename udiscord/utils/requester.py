from .exceptions import *
from . import log

from requests import Session, Response
from aiohttp import ClientSession, ClientResponse
from json import dumps

class Requester:
	def __init__(self, user_agent: str):
		self.web_api = "https://discord.com/api/v9"
		self.session = Session()
		self.user_agent = user_agent
		self.token = None
		self.userId = None

	def headers(self) -> dict:
		headers = {
			"content-type": "application/json",
			"user-agent": self.user_agent,
		}
		if self.token:headers["authorization"] = self.token
		return headers


	def make_request(self, method: str, endpoint: str, body: dict = None, allowed_code: int = 200, proxies: dict = None) -> Response:
		response = self.session.request(method, f"{self.web_api}{endpoint}", data=dumps(body) if body is not None else None, headers=self.headers(), proxies=proxies)
		log.debug(f"[https][{method}][{endpoint}][{response.status_code}]: {body}")
		return checkException(response.text) if response.status_code != allowed_code else response


	async def make_async_request(self, method: str, endpoint: str, body: dict = None, allowed_code: int = 200) -> ClientResponse:
		async with ClientSession() as asyncSession:
			response = await asyncSession.request(method, f"{self.web_api}{endpoint}", data=dumps(body) if body else None, headers=self.headers())
			log.debug(f"[https][{method}][{endpoint}][{response.status}]: {body}")
			return checkException(await response.text()) if response.status != allowed_code else response