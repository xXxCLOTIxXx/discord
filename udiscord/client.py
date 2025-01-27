from .utils.objects import *
from .utils.requester import Requester
from .utils import exceptions

from .ws import Socket

from json import loads

class Client(Socket):
	def __init__(self, proxies: dict = None, sock_trace: bool = False):
		self.req = Requester()
		self.proxies = proxies
		Socket.__init__(self, sock_trace=sock_trace)


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
		print(data)

		resp = LoginInfo(loads(self.req.make_request(method="POST", endpoint="/auth/login", body=data, proxies=self.proxies).text))
		self.req.token = resp.token
		self.connect()
		return resp


	def login_token(self, token: str):
		self.req.token = token
		info = self.conditional_start()
		self.connect()
		return info

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
		self.disconnect()
		return resp


	def get_channel_messages(self, channelId: int, size: int = 50):
		"""
		`Get a list of messages in a channel`
			**channelId - ID of the selected channel [TYPE: int]

			*size - Message list length [TYPE: int] [Default: 50]
		"""

		return ChannelMessages(loads(self.req.make_request(method="GET", endpoint=f"/channels/{channelId}/messages?limit={size}", proxies=self.proxies).text))

	def get_user_info(self, userId: int, with_mutual_guilds: bool = True, with_mutual_friends_count: bool = True):
		"""
		`Get user information`
			**userId - ID of the selected user [TYPE: int]

			*with_mutual_guilds - Get shared servers [TYPE: bool] [Default: True]
			*with_mutual_friends_count - Get mutual friends [TYPE: bool] [Default: True]
		"""

		return UserProfile(loads(self.req.make_request(method="GET", endpoint=f"/users/{userId}/profile?with_mutual_guilds={with_mutual_guilds}&with_mutual_friends_count={with_mutual_friends_count}", proxies=self.proxies).text))

	def get_my_channels(self):
		"""
		`Get a list of channels on an account`
		"""

		return Channels(loads(self.req.make_request(method="GET", endpoint=f"/users/@me/channels", proxies=self.proxies).text))

	def get_my_guilds(self):
		"""
		`Get the servers you belong to`
		"""

		return Guilds(loads(self.req.make_request(method="GET", endpoint=f"/users/@me/guilds", proxies=self.proxies).text))

	def send_message(self, channelId: int, message: str) -> dict:
		"""
		`Send a message to a channel`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
		"""

		data = {"content": message}
		return Message(loads(self.req.make_request(method="POST", endpoint=f"/channels/{channelId}/messages", body=data, proxies=self.proxies).text))


	def delete_message(self, channelId: int, messageId: int) -> dict:
		"""
		`Delete a message from a channel`
			**channelId - Channel ID [TYPE: int]
			**messageId - Message ID [TYPE: str]
		"""
		return self.req.make_request(method="DELETE", endpoint=f"/channels/{channelId}/messages/{messageId}", allowed_code=204, proxies=self.proxies).status_code


	def get_invite_info(self, invite_code: str, with_counts: bool = True, with_expiration: bool = True, with_permissions: bool = False):
		"""
		`Retrieve information about an invite`
			**invite_code - Invite code [TYPE: str]
			**with_counts - Include usage counts (default: True) [TYPE: bool]
			**with_expiration - Include expiration details (default: True) [TYPE: bool]
			**with_permissions - Include permissions information (default: False) [TYPE: bool]
		"""
		return Invite(self.req.make_request(method="GET", endpoint=f"/invites/{invite_code}?with_counts={with_counts}&with_expiration={with_expiration}&with_permissions={with_permissions}", proxies=self.proxies).json())
	
	def get_invites(self, channelId: int):
		"""
		`Retrieve all invites for a channel`
			**channelId - Channel ID [TYPE: int]
		"""
		return Invites(self.req.make_request(method="GET", endpoint=f"/channels/{channelId}/invites", proxies=self.proxies).json())


	def get_location_metadata(self):
		"""
		`Retrieve metadata about the current location`
		"""
		return LocationMetadata(self.req.make_request(method="GET", endpoint=f"/auth/location-metadata", proxies=self.proxies).json())
	
	def conditional_start(self):
		"""
		`Get information about the current session`
		"""
		return LoginInfo(self.req.make_request(method="POST", endpoint=f"/auth/conditional/start", proxies=self.proxies).json())