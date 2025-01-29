from .utils.objects import *
from .utils.requester import Requester
from .utils import exceptions

from .ws import Socket, EventType

from json import loads

class Client(Socket):
	"""
	The main client class of the library for Discord user bots.

	Inherits from Socket to work with Discord's WebSocket API in real time.  
	Provides methods for automating actions, managing the account, and interacting with Discord.

	Arguments:
	- proxies: dict = None — proxy for the connection.
	- sock_trace: bool = False — enables WebSocket connection debugging.

	Data available in the class (besides functions):
	- Client.token: str — token after authorization.
	- Client.userId: int — account ID after logging in.
	- Client.account: AccountInfo — a class containing all account information received after connecting to the socket.
	"""

	def __init__(self, proxies: dict = None, sock_trace: bool = False):
		self.req = Requester()
		self.proxies = proxies
		self.account: AccountInfo = AccountInfo({})
		Socket.__init__(self, sock_trace=sock_trace)

		self.add_handler(EventType.READY, self._on_connect)
	

	def __repr__(self) -> str:
		attrs = [
			('token', self.token),
			('userId', self.userId)
		]
		inner = ' '.join('%s=%r' % t for t in attrs)
		return f"<class '{self.__class__.__name__}' {inner}>"


	def __del__(self):
		if self.token:
			self.logout()



	def _on_connect(self, event: AccountInfo):
		self.account = event

	@property
	def token(self):
		return self.req.token

	@property
	def userId(self):
		return self.req.userId


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

		resp = LoginInfo(loads(self.req.make_request(method="POST", endpoint="/auth/login", body=data, proxies=self.proxies).text))
		self.req.token = resp.token
		self.req.userId = resp.userId
		self.connect()
		return resp


	def login_token(self, token: str):
		"""
		`Log in to your account by token`
		"""
		self.req.token = token
		info = self.conditional_start()
		if not info.token: raise exceptions.InvalidAuthorizationToken(info.data)
		self.req.userId = info.userId
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
		self.req.userId = None
		if self.active:self.disconnect()
		self.account = AccountInfo({})
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

	def edit_message(self, channelId: int, message: str, messageId: int) -> dict:
		"""
		`Edit message`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
			**messageId - Message ID [TYPE: int]
		"""

		data = {"content": message}
		return Message(loads(self.req.make_request(method="PATCH", endpoint=f"/channels/{channelId}/messages/{messageId}", body=data, proxies=self.proxies).text))

	def reply_message(self, channelId: int, message: str, messageId: int, guildId: int = None) -> dict:
		"""
		`Reply to message`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
			**messageId - Message ID [TYPE: int]
			**guildId - server ID [TYPE: int | None]
		"""
		data = {"content": message, "message_reference": {
			"channel_id": channelId,
			"message_id": messageId
		}}
		if guildId: data["guild_id"]=guildId
		return Message(loads(self.req.make_request(method="POST", endpoint=f"/channels/{channelId}/messages", body=data, proxies=self.proxies).text))



	def delete_message(self, channelId: int, messageId: int) -> dict:
		"""
		`Delete a message from a channel`
			**channelId - Channel ID [TYPE: int]
			**messageId - Message ID [TYPE: int]
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