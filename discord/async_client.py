from .utils.requester import Requester
from .utils import objects, exceptions
from .async_socket import AsyncSocket

from json import loads

from asyncio import get_event_loop, new_event_loop

class AsyncClient(AsyncSocket):
	def __init__(self, socket_debug: bool = False):
		self.req = Requester()
		AsyncSocket.__init__(self, headers=self.req.headers, debug=socket_debug)

	async def login(self, login: str, password: str, login_source: str = None, gift_code_sku_id: str = None):
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

		resp = await self.req.make_async_request(method="POST", endpoint="/auth/login", body=data)
		resp = objects.LoginInfo(loads(await resp.text()))
		self.req.token = resp.token
		#await self.connect()
		return resp

	async def logout(self):
		"""
		`Sign out of your account`
		"""

		data = {
			"provider": None,
			"voip_provider": None
		}

		resp = await self.req.make_async_request(method="POST", endpoint="/auth/logout", body=data, allowed_code=204)
		self.req.token = None
		return resp.status




	async def get_channel_messages(self, channelId: int, size: int = 50):
		"""
		`Get a list of messages in a channel`
			**channelId - ID of the selected channel [TYPE: int]

			*size - Message list length [TYPE: int] [Default: 50]
		"""

		resp = await self.req.make_async_request(method="GET", endpoint=f"/channels/{channelId}/messages?limit={size}")
		return objects.ChannelMessages(loads(await resp.text()))

	async def get_user_info(self, userId: int, with_mutual_guilds: bool = True, with_mutual_friends_count: bool = True):
		"""
		`Get user information`
			**userId - ID of the selected user [TYPE: int]

			*with_mutual_guilds - Get shared servers [TYPE: bool] [Default: True]
			*with_mutual_friends_count - Get mutual friends [TYPE: bool] [Default: True]
		"""

		resp = await self.req.make_async_request(method="GET", endpoint=f"/users/{userId}/profile?with_mutual_guilds={with_mutual_guilds}&with_mutual_friends_count={with_mutual_friends_count}")
		return objects.UserProfile(loads(await resp.text()))

	async def get_my_channels(self):
		"""
		`Get a list of channels on an account`
		"""

		resp = await self.req.make_async_request(method="GET", endpoint=f"/users/@me/channels")
		return objects.Channels(loads(await resp.text()))



	async def get_my_guilds(self):
		"""
		`Get the servers you belong to`
		"""

		resp = await self.req.make_async_request(method="GET", endpoint=f"/users/@me/guilds")
		return objects.Guilds(loads(await resp.text()))

	async def send_message(self, channelId: int, message: str) -> dict:
		"""
		`Send a message to a channel`
			**channelId - Channel ID [TYPE: int]
			**message - Your message [TYPE: str]
		"""

		data = {"content": message}
		resp = await self.req.make_async_request(method="POST", endpoint=f"/channels/{channelId}/messages", body=data)
		return objects.Message(loads(await resp.text()))


	async def delete_message(self, channelId: int, messageId: int) -> dict:
		"""
		`Delete a message from a channel`
			**channelId - Channel ID [TYPE: int]
			**messageId - Message ID [TYPE: str]
		"""

		resp = await self.req.make_async_request(method="DELETE", endpoint=f"/channels/{channelId}/messages/{messageId}", allowed_code=204)
		return await resp.status