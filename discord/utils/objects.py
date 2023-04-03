


class LoginInfo:
	def __init__(self, data: dict = {}):
		self.json = data
		user_settings = self.json.get("user_settings")
		
		self.token = self.json.get("token")
		self.userId = self.json.get("user_id")
		self.locale = user_settings.get("locale")
		self.theme = user_settings.get("theme")

class Message:
	def __init__(self, data: dict = {}):
		self.json = data
		self.messageId = self.json.get("id")
		self.messageType = self.json.get("type")
		self.content = self.json.get("content")
		self.channelId = self.json.get("channel_id")
		self.attachments = self.json.get("attachments", [])
		self.embeds = self.json.get("embeds", [])
		self.mentions = self.json.get("mentions", [])
		self.mention_roles = self.json.get("mention_roles", [])
		self.pinned = self.json.get("pinned")
		self.mention_everyone = self.json.get("mention_everyone")
		self.tts = self.json.get("tts")
		self.timestamp = self.json.get("timestamp")
		self.edited_timestamp = self.json.get("edited_timestamp")
		self.flags = self.json.get("flags")
		self.components = self.json.get("components", [])
		self.author = self.Author(self.json.get("author", {}))
		self.referenced_message = self.json.get("referenced_messages")

	class Author:
		def __init__(self, data: dict = {}):
			self.json = data
			self.userId = self.json.get("id")
			self.username = self.json.get("username")
			self.global_name = self.json.get("global_name")
			self.display_name = self.json.get("display_name")
			self.avatar = self.json.get("avatar")
			self.avatar_decoration = self.json.get("avatar_decoration")
			self.discriminator = self.json.get("discriminator")
			self.public_flags = self.json.get("public_flags")




class ChannelMessages:
	def __init__(self, data: list = []):
		self.json = data
		self.size = len(self.json)
		self.messages = list()
		for message in self.json:
			self.messages.append(Message(message))



class UserProfile:
	def __init__(self, data: dict = {}):
		self.json = data
		user = self.json.get("user", {})

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
		self.premium_since = self.json.get("premium_since")
		self.premium_type = self.json.get("premium_type")
		self.premium_guild_since = self.json.get("premium_guild_since")
		self.profile_themes_experiment_bucket = self.json.get("profile_themes_experiment_bucket")
		self.mutual_friends_count = self.json.get("mutual_friends_count")
		self.mutual_guilds = self.json.get("mutual_guilds")
		self.connected_accounts = self.json.get("connected_accounts")


class Channels:
	def __init__(self, data: list = []):
		self.json = data
		self.size = len(self.json)
		self.channels = list()
		for channel in self.json:
			self.channels.append(self.ChannelInfo(channel))


	class ChannelInfo:
		def __init__(self, data: dict = {}):
			self.json=data
			self.channelId = self.json.get("id")
			self.channelType = self.json.get("type")
			self.last_message_id = self.json.get("last_message_id")
			self.flags = self.json.get("flags")
			self.name = self.json.get("name")
			self.icon = self.json.get("icon")
			self.owner_id = self.json.get("owner_id")
			self.channelMembers = list()
			for member in self.json.get("recipients", {}):
				self.channelMembers.append(UserProfile(member))
			self.members_size = len(self.channelMembers)

class Guilds:
	def __init__(self, data: list = []):
		self.json = data
		self.size = len(self.json)
		self.guilds = list()
		for guild in self.json:
			self.guilds.append(self.GuildInfo(guild))


	class GuildInfo:
		def __init__(self, data: dict = {}):
			self.json = data
			self.guildId = self.json.get("id")
			self.guildName = self.json.get("name")
			self.icon = self.json.get("icon")
			self.owner = self.json.get("owner")
			self.permissions = self.json.get("permissions")
			self.features = self.json.get("features", [])
