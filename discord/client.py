from .utils.requester import Requester
from .utils import objects, exceptions

from .socket import Socket

from json import loads

class Client(Socket):
	def __init__(self, proxies: dict = None, socket_debug: bool = False, sock_trace: bool = False):
		self.req = Requester()
		self.proxies = proxies

		Socket.__init__(self, headers=self.req.headers, sock_trace=sock_trace, debug=socket_debug)


	def login(self, login: str, password: str, login_source: str = None, gift_code_sku_id: str = None):
		"""
		`Log in to your account`
		"""

		data = {
			"login": login,
			"password": password,
			"undelete": False,
			"captcha_key": None,
			"login_source": login_source,
			"gift_code_sku_id": gift_code_sku_id
		}

		resp = objects.LoginInfo(loads(self.req.make_request(method="POST", endpoint="/auth/login", body=data, proxies=self.proxies).text))
		self.req.token = resp.token
		#self.connect()
		return resp

	def logout(self):
		"""
		`Sign out of your account`
		"""

		data = {
			"provider": None,
			"voip_provider": None
		}

		resp = self.req.make_request(method="POST", endpoint="/auth/logout", body=data, allowed_code=204, proxies=self.proxies).status_code
		self.req.token = None
		return resp


	def get_channel_messages(self, channelId: int, size: int = 50):
		"""
		`Get a list of messages in a channel`
			**channelId - ID of the selected channel [TYPE: int]

			*size - Message list length [TYPE: int] [Default: 50]
		"""

		return objects.ChannelMessages(loads(self.req.make_request(method="GET", endpoint=f"/channels/{channelId}/messages?limit={size}", proxies=self.proxies).text))

	def get_user_info(self, userId: int, with_mutual_guilds: bool = True, with_mutual_friends_count: bool = True):
		"""
		`Get user information`
			**userId - ID of the selected user [TYPE: int]

			*with_mutual_guilds - Get shared servers [TYPE: bool] [Default: True]
			*with_mutual_friends_count - Get mutual friends [TYPE: bool] [Default: True]
		"""

		return objects.UserProfile(loads(self.req.make_request(method="GET", endpoint=f"/users/{userId}/profile?with_mutual_guilds={with_mutual_guilds}&with_mutual_friends_count={with_mutual_friends_count}", proxies=self.proxies).text))

	def get_my_channels(self):
		"""
		`Get a list of channels on an account`
		"""

		return objects.Channels(loads(self.req.make_request(method="GET", endpoint=f"/users/@me/channels", proxies=self.proxies).text))



	def get_my_guilds(self):
		"""
		`Get the servers you belong to`
		"""

		return objects.Guilds(loads(self.req.make_request(method="GET", endpoint=f"/users/@me/guilds", proxies=self.proxies).text))

	def send_message(self, channelId: int, message: str) -> dict:
		"""
		`Send a message to a channel`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
		"""

		data = {"content": message}
		return objects.Message(loads(self.req.make_request(method="POST", endpoint=f"/channels/{channelId}/messages", body=data, proxies=self.proxies).text))


	def delete_message(self, channelId: int, messageId: int) -> dict:
		"""
		`Delete a message from a channel`
			**channelId - Channel ID [TYPE: int]
			**messageId - Message ID [TYPE: str]
		"""
		return self.req.make_request(method="DELETE", endpoint=f"/channels/{channelId}/messages/{messageId}", allowed_code=204, proxies=self.proxies).status_code