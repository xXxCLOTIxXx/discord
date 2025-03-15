from . import UserProfile, Message

class Channels:
	def __init__(self, data: list = []):
		self.data = data
		self.size = len(self.data)
		self.channels = list()
		for channel in self.data:
			self.channels.append(Channel(channel))


class Channel:
	def __init__(self, data: dict = {}):
		self.data=data
		self.channelId = self.data.get("id")
		self.channelType = self.data.get("type")
		self.last_message_id = self.data.get("last_message_id")
		self.flags = self.data.get("flags")
		self.name = self.data.get("name")
		self.icon = self.data.get("icon")
		self.owner_id = self.data.get("owner_id")
		self.channelMembers = list()
		for member in self.data.get("recipients", {}):
			self.channelMembers.append(UserProfile(member))
		self.members_size = len(self.channelMembers)


class ChannelMessages:
	def __init__(self, data: list = []):
		self.data = data
		self.size = len(self.data)
		self.messages = list()
		for message in self.data:
			self.messages.append(Message(message))
