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

	def headers(self, headers: dict = None) -> dict:
		default_headers = {
			"content-type": "application/json",
			"user-agent": self.user_agent,
		}
		if self.token:
			default_headers["authorization"] = self.token
		if headers: default_headers.update(headers)
		return default_headers



	def make_request(self, method: str, endpoint: str = None, body: dict | bytes = None, allowed_code: int = 200, proxies: dict = None, headers: dict = None, api: str = None) -> Response:
		response = self.session.request(method, f"{api or self.web_api}{endpoint or ''}", data=dumps(body) if isinstance(body, dict) else body if body is not None else None, headers=self.headers(headers), proxies=proxies)
		log.debug(f"[https][{method}][{api or ''}{endpoint or ''}][{response.status_code}]: {len(body) if isinstance(body, bytes) else body}")
		return checkException(response.text) if response.status_code != allowed_code else response


	async def make_async_request(self, method: str, endpoint: str = None, body: dict = None, allowed_code: int = 200, headers: dict = None , api: str = None) -> ClientResponse:
		async with ClientSession() as asyncSession:
			response = await asyncSession.request(method, f"{api or self.web_api}{endpoint or ''}", data=dumps(body) if body else None, headers=self.headers(headers))
			log.debug(f"[https][{method}][{endpoint or ''}][{response.status}]: {body}")
			return checkException(await response.text()) if response.status != allowed_code else response