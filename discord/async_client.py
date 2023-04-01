from .utils.requester import Requester
from .utils import objects, exceptions
from json import loads

from asyncio import get_event_loop, new_event_loop

class AsyncClient:
	def __init__(self):
		self.req = Requester()

	async def login(self, login: str, password: str, login_source: str = None, gift_code_sku_id: str = None):

		data = {
			"login": login,
			"password": password,
			"undelete": False,
			"captcha_key": None,
			"login_source": login_source,
			"gift_code_sku_id": gift_code_sku_id
		}

		resp = await self.req.make_async_request(method="POST", endpoint="/auth/login", body=data)
		resp = objects.LoginInfo(loads(await resp.text()))
		self.req.token = resp.token
		return resp

	async def logout(self):

		data = {
			"provider": None,
			"voip_provider": None
		}

		resp = await self.req.make_async_request(method="POST", endpoint="/auth/logout", body=data, allowed_code=204)
		self.req.token = None
		return resp.status

