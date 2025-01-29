
class Message:
	def __init__(self, data: dict = {}):
		self.data = data
		self.messageId = self.data.get("id")
		self.messageType = self.data.get("type")
		self.content = self.data.get("content")
		self.channelId = self.data.get("channel_id")
		self.attachments = self.data.get("attachments", [])
		self.embeds = self.data.get("embeds", [])
		self.mentions = self.data.get("mentions", [])
		self.mention_roles = self.data.get("mention_roles", [])
		self.pinned = self.data.get("pinned")
		self.mention_everyone = self.data.get("mention_everyone")
		self.tts = self.data.get("tts")
		self.timestamp = self.data.get("timestamp")
		self.edited_timestamp = self.data.get("edited_timestamp")
		self.flags = self.data.get("flags")
		self.components = self.data.get("components", [])
		self.author = self.Author(self.data.get("author", {}))
		self.referenced_message = self.data.get("referenced_messages")
		self.guildId = self.data.get("guild_id")

	class Author:
		def __init__(self, data: dict = {}):
			self.data = data
			self.userId = self.data.get("id")
			self.username = self.data.get("username")
			self.global_name = self.data.get("global_name")
			self.display_name = self.data.get("display_name")
			self.avatar = self.data.get("avatar")
			self.avatar_decoration = self.data.get("avatar_decoration")
			self.discriminator = self.data.get("discriminator")
			self.public_flags = self.data.get("public_flags")