from .utils.requester import Requester
from .utils import objects, exceptions
from json import loads

class Client:
	def __init__(self):
		self.req = Requester()


	def login(self, login: str, password: str, login_source: str = None, gift_code_sku_id: str = None):

		data = {
			"login": login,
			"password": password,
			"undelete": False,
			"captcha_key": None,
			"login_source": login_source,
			"gift_code_sku_id": gift_code_sku_id
		}

		resp = objects.LoginInfo(loads(self.req.make_request(method="POST", endpoint="/auth/login", body=data).text))
		self.req.token = resp.token
		return resp

	def logout(self):

		data = {
			"provider": None,
			"voip_provider": None
		}

		resp = self.req.make_request(method="POST", endpoint="/auth/logout", body=data, allowed_code=204).status_code
		self.req.token = None
		return resp

