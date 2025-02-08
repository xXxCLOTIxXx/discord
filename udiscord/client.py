from .utils.objects import *
from .utils.requester import Requester
from .utils import exceptions

from .ws import Socket, EventType

class Client(Socket):
	"""
	The main client class of the library for Discord user bots.
	Inherits from Socket to work with Discord's WebSocket API in real time.  
	Provides methods for automating actions, managing the account, and interacting with Discord.

	Arguments :
	- proxies: dict = None — proxy for the connection.
	- socket_enable: bool = True — whether to connect the socket (if you disconnect it, events and other related things will not work).
	- sock_trace: bool = False — enables WebSocket connection debugging.
	- user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0" — user agent string used for requests.
	- os: str = "Windows" — operating system identifier.
	- browser: str = "Firefox" — browser identifier.
	- device: str = "" — device identifier.

	Data available in the class (besides functions):
	- Client.token: str — token after authorization.
	- Client.userId: int — account ID after logging in.
	- Client.account: AccountInfo — a class containing all account information received after connecting to the socket.
	"""


	def __init__(self, proxies: dict = None, socket_enable: bool = True, sock_trace: bool = False,
			  user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0", os: str = "Windows", browser: str = "Firefox", device: str = ""):
		self.socket_enable=socket_enable
		self.req = Requester(user_agent)
		self.proxies = proxies
		self.account: AccountInfo = AccountInfo({})
		Socket.__init__(self, os, browser, device, sock_trace)

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
			try:self.logout()
			except: pass



	def _on_connect(self, event: AccountInfo):
		self.account = event

	@property
	def token(self):
		return self.req.token

	@property
	def userId(self):
		return self.req.userId

	@property
	def user_agent(self):
		return self.req.user_agent



	def login(self, login: str, password: str, login_source: str = None, gift_code_sku_id: str = None) -> LoginInfo:
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

		resp = LoginInfo(self.req.make_request(method="POST", endpoint="/auth/login", body=data, proxies=self.proxies).json())
		self.req.token = resp.token
		self.req.userId = resp.userId
		if self.socket_enable:self.connect()
		return resp


	def login_token(self, token: str) -> LoginInfo:
		"""
		`Log in to your account by token`
		"""
		self.req.token = token
		info = self.conditional_start()
		if not info.token: raise exceptions.InvalidAuthorizationToken(info.data)
		self.req.userId = info.userId
		if self.socket_enable:self.connect()
		return info

	def qrcode_auth(self, code: str, temporary_token: bool = False) -> int:
		"""
		Authenticates the user via QR code.

		This method performs remote authentication using a QR code scanned from 
		the Discord app (e.g., https://discord.com/ra/{code}).

		:param code: The unique authentication code from the QR link.
		:param temporary_token: If True, a temporary token will be issued instead of a permanent session.
		:return: The HTTP status code of the authentication request.
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		handshake = self.create_remote_auth_handshake(code)
		return self.remote_auth(handshake, temporary_token)


	def create_remote_auth_handshake(self, code: str) -> str:
		"""
		Initiates a remote authentication handshake.

		Sends a request to begin the authentication process using the QR code.

		:param code: The authentication code extracted from the QR link.
		:return: A handshake token required to complete authentication.
		"""
		data = {
			"fingerprint": code
		}
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="POST", endpoint="/users/@me/remote-auth", body=data, proxies=self.proxies).json().get("handshake_token")


	def remote_auth(self, handshake: str, temporary_token: bool = False) -> int:
		"""
		Completes remote authentication using the handshake token.

		:param handshake: The handshake token obtained from `create_remote_auth_handshake`.
		:param temporary_token: If True, a temporary token will be issued.
		:return: The HTTP status code (204 on success).
		"""
		data = {
			"handshake_token": handshake,
			"temporary_token": temporary_token
		}
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="POST", endpoint="/users/@me/remote-auth/finish", body=data, proxies=self.proxies, allowed_code=204).status_code



	def logout(self) -> int:
		"""
		`Sign out of your account`

		:return: HTTP status code of the request. (204 on success)
		"""

		data = {
			"provider": None,
			"voip_provider": None
		}
		if not self.token: raise exceptions.UnauthorizedClientError
		resp = self.req.make_request(method="POST", endpoint="/auth/logout", body=data, allowed_code=204, proxies=self.proxies).status_code
		self.req.token = None
		self.req.userId = None
		if self.active:self.disconnect()
		self.account = AccountInfo({})
		return resp


	def get_channel_messages(self, channelId: int, size: int = 50) -> ChannelMessages:
		"""
		`Get a list of messages in a channel`
			**channelId - ID of the selected channel [TYPE: int]

			*size - Message list length [TYPE: int] [Default: 50]
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return ChannelMessages(self.req.make_request(method="GET", endpoint=f"/channels/{channelId}/messages?limit={size}", proxies=self.proxies).json())

	def get_user_info(self, userId: int, with_mutual_guilds: bool = True, with_mutual_friends_count: bool = True) -> UserProfile:
		"""
		`Get user information`
			**userId - ID of the selected user [TYPE: int]

			*with_mutual_guilds - Get shared servers [TYPE: bool] [Default: True]
			*with_mutual_friends_count - Get mutual friends [TYPE: bool] [Default: True]
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return UserProfile(self.req.make_request(method="GET", endpoint=f"/users/{userId}/profile?with_mutual_guilds={with_mutual_guilds}&with_mutual_friends_count={with_mutual_friends_count}", proxies=self.proxies).json())


	def get_me_info(self) -> dict:
		"""
		Retrieves information about the current user.

		:return: A dictionary containing the user's profile data.
		"""
		#if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="GET", endpoint="/users/@me", proxies=self.proxies).json()


	def online_status(self, mode: int = 0) -> str:
		"""
		Sets the user's online status.

		Available statuses:
		- 0: Online
		- 1: Idle
		- 2: Do Not Disturb
		- 3: Invisible

		:param mode: Numeric status code (0-3).
		:return: The Base64-encoded settings value.
		:raises exceptions.WrongModeError: If an invalid status code is provided.
		"""
		modes = {
			0: "WgoKCAoGb25saW5l",  # online
			1: "WggKBgoEaWRsZQ==",  # idle
			2: "WgcKBQoDZG5k",  # do not disturb
			3: "Wg0KCwoJaW52aXNpYmxl"  # invisible
		}

		if mode not in modes:
			raise exceptions.WrongModeError(mode)
		if not self.token: raise exceptions.UnauthorizedClientError

		data = {"settings": modes.get(mode)}
		return self.req.make_request(method="PATCH", endpoint="/users/@me/settings-proto/1", body=data, proxies=self.proxies).json()["settings"]

	def get_my_channels(self) -> Channels:
		"""
		`Get a list of channels on an account`
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return Channels(self.req.make_request(method="GET", endpoint=f"/users/@me/channels", proxies=self.proxies).json())

	def get_my_guilds(self) -> Guilds:
		"""
		`Get the servers you belong to`
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return Guilds(self.req.make_request(method="GET", endpoint=f"/users/@me/guilds", proxies=self.proxies).json())

	def send_message(self, channelId: int, message: str) -> Message:
		"""
		`Send a message to a channel`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		data = {"content": message}
		return Message(self.req.make_request(method="POST", endpoint=f"/channels/{channelId}/messages", body=data, proxies=self.proxies).json())

	def edit_message(self, channelId: int, message: str, messageId: int) -> Message:
		"""
		`Edit message`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
			**messageId - Message ID [TYPE: int]
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		data = {"content": message}
		return Message(self.req.make_request(method="PATCH", endpoint=f"/channels/{channelId}/messages/{messageId}", body=data, proxies=self.proxies).json())

	def reply_message(self, channelId: int, message: str, messageId: int, guildId: int = None) -> Message:
		"""
		`Reply to message`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
			**messageId - Message ID [TYPE: int]
			**guildId - server ID [TYPE: int | None]
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		data = {"content": message, "message_reference": {
			"channel_id": channelId,
			"message_id": messageId
		}}
		if guildId: data["guild_id"]=guildId
		return Message(self.req.make_request(method="POST", endpoint=f"/channels/{channelId}/messages", body=data, proxies=self.proxies).json())



	def delete_message(self, channelId: int, messageId: int) -> int:
		"""
		`Delete a message from a channel`
			**channelId - Channel ID [TYPE: int]
			**messageId - Message ID [TYPE: int]
			
			:return: HTTP status code of the request. (204 on success)
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="DELETE", endpoint=f"/channels/{channelId}/messages/{messageId}", allowed_code=204, proxies=self.proxies).status_code


	def get_invite_info(self, invite_code: str, with_counts: bool = True, with_expiration: bool = True, with_permissions: bool = False) -> Invite:
		"""
		`Retrieve information about an invite`
			**invite_code - Invite code [TYPE: str]
			**with_counts - Include usage counts (default: True) [TYPE: bool]
			**with_expiration - Include expiration details (default: True) [TYPE: bool]
			**with_permissions - Include permissions information (default: False) [TYPE: bool]
		"""
		return Invite(self.req.make_request(method="GET", endpoint=f"/invites/{invite_code}?with_counts={with_counts}&with_expiration={with_expiration}&with_permissions={with_permissions}", proxies=self.proxies).json())
	
	def get_invites(self, channelId: int) -> Invites:
		"""
		`Retrieve all invites for a channel`
			**channelId - Channel ID [TYPE: int]
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return Invites(self.req.make_request(method="GET", endpoint=f"/channels/{channelId}/invites", proxies=self.proxies).json())


	def create_invite(self, channelId: int, max_age: int = 86400) -> Invite:
		"""
		Creates an invite for the specified channel.

		:param channelId: The ID of the channel for which the invite is created.
		:param max_age: The invite's lifetime in seconds (default is 86400 seconds = 24 hours).
		:return: An Invite object.
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		Invite(self.req.make_request(method="POST", endpoint=f"/channels/{channelId}/invites", proxies=self.proxies, body={"max_age": max_age}).json())


	def leave_guild(self, guildId: int, lurking: bool = False) -> int:
		"""
		Leaves a guild.

		:param guildId: The ID of the guild to leave.
		:param lurking: If True, the user will remain in the guild in a "lurking" (invisible presence) mode.
		:return: HTTP status code of the request. (204 on success)
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="DELETE", endpoint=f"/users/@me/guilds/{guildId}", allowed_code=204, proxies=self.proxies, body={"lurking": lurking}).status_code


	def conditional_start(self) -> LoginInfo:
		"""
		`Get information about the current session`
		"""
		return LoginInfo(self.req.make_request(method="POST", endpoint=f"/auth/conditional/start", proxies=self.proxies).json())

	def get_location_metadata(self) -> LocationMetadata:
		"""
		`Retrieve metadata about the current location`
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return LocationMetadata(self.req.make_request(method="GET", endpoint=f"/auth/location-metadata", proxies=self.proxies).json())

	def check_username_taken(self, username	: str) -> bool:
		"""
		`Checks if the username is busy`

		:param username: username for check
		:return: True or False
		"""
		return self.req.make_request(method="POST", endpoint="/users/@me/pomelo-attempt" if self.token else "/unique-username/username-attempt-unauthed", proxies=self.proxies, body={"username": username}).json()["taken"]


	def resend_verify_code(self) -> int:
		"""
		`resend the confirmation code by email`

		:return: HTTP status code of the request. (204 on success)
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="POST", endpoint=f"/auth/verify/resend", proxies=self.proxies, allowed_code=204).status_code
	
	def forgot_password_request(self, email: str) -> int:
		"""
		Sends a password reset email.

		:param email: The email address associated with the account.
		:return: HTTP status code of the request. (204 on success)
		"""
		return self.req.make_request(method="POST", endpoint=f"/auth/forgot", body={"login": email}, proxies=self.proxies, allowed_code=204).status_code
	
	def edit_profile(self, bio: str = None, pronouns: str = None, accent_color: str = None) -> UserProfile:
		"""
		Edits the user's profile.

		:param bio: New biography text (optional).
		:param pronouns: New pronouns (optional) (like "he / his").
		:param accent_color: New accent color in hex format (e.g., "#FF5733") (optional).
		:return: UserProfile object.
		:raises: exceptions.ArgumentNotSpecifiedError if no parameters are provided.
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		data = {}
		if bio is None and pronouns is None and accent_color is None: raise exceptions.ArgumentNotSpecifiedError
		if bio: data["bio"]=bio
		if pronouns: data["pronouns"]=pronouns
		if accent_color: data["accent_color"]=int(accent_color[1:], 16)
		return UserProfile(self.req.make_request(method="PATCH", endpoint=f"/users/@me/profile", proxies=self.proxies, body=data).json())


	def delete_friend(self, userId: int) -> int:
		"""
		Removes a user from the friend list.

		:param userId: The ID of the user to remove.
		:return: HTTP status code of the request. (204 on success)
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="DELETE", endpoint=f"/users/@me/relationships/{userId}", proxies=self.proxies, allowed_code=204).status_code

	def accept_friend_request(self, userId: int) -> int:
		"""
		Accepts a friend request from a user.

		:param userId: The ID of the user whose request is being accepted.
		:return: HTTP status code of the request. (204 on success)
		"""
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.req.make_request(method="PUT", endpoint=f"/users/@me/relationships/{userId}", proxies=self.proxies, body={}, allowed_code=204).status_code
	
	def ignore_friend_request(self, userId: int) -> int:
		"""
		Ignores (declines) a friend request from a user.

		:param userId: The ID of the user whose request is being ignored.
		:return: HTTP status code of the request. (204 on success)
		""" 
		if not self.token: raise exceptions.UnauthorizedClientError
		return self.delete_friend(userId)
