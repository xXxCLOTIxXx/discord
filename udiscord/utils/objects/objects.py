


class LoginInfo:
	def __init__(self, data: dict = {}):
		self.data = data
		user_settings = self.data.get("user_settings", {})
		
		self.token = self.data.get("token")
		self.userId = self.data.get("user_id")
		self.locale = user_settings.get("locale")
		self.theme = user_settings.get("theme")
		self.ticket: str = self.data.get("ticket")
		self.challenge: str = self.data.get("challenge")

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




class ChannelMessages:
	def __init__(self, data: list = []):
		self.data = data
		self.size = len(self.data)
		self.messages = list()
		for message in self.data:
			self.messages.append(Message(message))



class UserProfile:
	def __init__(self, data: dict = {}):
		self.data = data
		user = self.data.get("user", {})

		self.userId = user.get("id")
		self.username = user.get("username")
		self.global_name = user.get("global_name")
		self.display_name = user.get("display_name")
		self.avatar = user.get("avatar")
		self.avatar_decoration = user.get("avatar_decoration")
		self.discriminator = user.get("discriminator")
		self.public_flags = user.get("public_flags")
		self.flags = user.get("flags")
		self.banner = user.get("banner")
		self.banner_color = user.get("banner_color")
		self.accent_color = user.get("accent_color")
		self.bio = user.get("bio")
		self.premium_since = self.data.get("premium_since")
		self.premium_type = self.data.get("premium_type")
		self.premium_guild_since = self.data.get("premium_guild_since")
		self.profile_themes_experiment_bucket = self.data.get("profile_themes_experiment_bucket")
		self.mutual_friends_count = self.data.get("mutual_friends_count")
		self.mutual_guilds = self.data.get("mutual_guilds")
		self.connected_accounts = self.data.get("connected_accounts")


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

class Guilds:
	def __init__(self, data: list = []):
		self.data = data
		self.size = len(self.data)
		self.guilds: list[Guild] = list()
		for guild in self.data:
			self.guilds.append(Guild(guild))


class Guild:
	def __init__(self, data: dict = {}):
		self.data = data
		self.guildId = self.data.get("id")
		self.guildName = self.data.get("name")
		self.icon = self.data.get("icon")
		self.owner = self.data.get("owner")
		self.permissions = self.data.get("permissions")
		self.features = self.data.get("features", [])
