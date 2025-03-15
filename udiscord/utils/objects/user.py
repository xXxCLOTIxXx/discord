



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



class BannedUser:
	def __init__(self, data: dict):
		self.data = data

		user: dict = self.data.get("user", {})

		self.userId = user.get("id")
		self.username = user.get("username")
		self.avatar = user.get("avatar")
		self.global_name = user.get("global_name")
		self.discriminator = user.get("discriminator")
		self.public_flags = user.get("public_flags")
		self.flags = user.get("flags")
		self.banner = user.get("banner")
		self.accent_color = user.get("accent_color")
		self.banner_color = user.get("banner_color")
		self.collectibles = user.get("collectibles")
		self.avatar_decoration_data = user.get("avatar_decoration_data")
		self.primary_guild = user.get("primary_guild")
		self.clan = user.get("clan")
		self.reason = data.get("reason")


class AvatarDecorationData:
	def __init__(self, data: dict):
		self.data: dict = data
		self.sku_id: str = data.get("sku_id")
		self.expires_at: int = data.get("expires_at")
		self.asset: str = data.get("asset")