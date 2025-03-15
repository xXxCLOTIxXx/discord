from .. import AvatarDecorationData


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


class ConnectedAccount: 
	def __init__(self, data: dict):
		self.data: dict = data
		self.visibility: int = data.get("visibility")
		self.verified: bool = data.get("verified")
		self.type: str = data.get("type")
		self.two_way_link: bool = data.get("two_way_link")
		self.show_activity: bool = data.get("show_activity")
		self.revoked: bool = data.get("revoked")
		self.name: bool = data.get("name")
		self.metadata_visibility: int = data.get("metadata_visibility")
		self.id: int = data.get("id")
		self.friend_sync: bool = data.get("friend_sync")



class User:
	def __init__(self, data: dict):
		self.data: dict = data
		self.username: str = data.get("username")
		self.public_flags: int = data.get("public_flags")
		self.primary_guild = data.get("primary_guild")
		self.id: str = data.get("id")
		self.global_name: str = data.get("global_name")
		self.discriminator: str = data.get("discriminator")
		self.clan = data.get("clan")
		self.avatar_decoration_data = AvatarDecorationData(data.get("avatar_decoration_data", {}) or {})
		self.avatar: str = data.get("avatar")



class Profile:
	def __init__(self, data: dict):
		self.data: dict = data
		self.verified: bool = data.get("verified")
		self.username: str = data.get("username")
		self.purchased_flags: int = data.get("purchased_flags")
		self.pronouns: str = data.get("pronouns")
		self.primary_guild = data.get("primary_guild")
		self.premium_type: int = data.get("premium_type")
		self.premium: bool = data.get("premium")
		self.phone: int = data.get("phone")
		self.nsfw_allowed: bool = data.get("nsfw_allowed")
		self.mobile: bool = data.get("mobile")
		self.mfa_enabled: bool = data.get("mfa_enabled")
		self.id: int = data.get("id")
		self.global_name: str = data.get("global_name")
		self.flags: int = data.get("flags")
		self.email: int = data.get("email")
		self.discriminator: str = data.get("discriminator")
		self.desktop: bool = data.get("desktop")
		self.clan = data.get("clan")
		self.bio: str = data.get("bio")
		self.banner_color: str = data.get("banner_color")
		self.banner = data.get("banner")
		self.avatar_decoration_data = data.get("avatar_decoration_data")
		self.avatar: str = data.get("avatar")
		self.accent_color: int = data.get("accent_color")



class Session:
	def __init__(self, data: dict):
		self.data = data
		self.status: str = data.get("status")
		self.session_id: str = data.get("session_id")
		self.activities: list = data.get("activities", [])
		self.id_hash: str = data.get("id_hash")
		self.approx_last_used_time: str = data.get("approx_last_used_time")

		client_info = data.get("client_info", {})
		self.version: int = client_info.get("version")
		self.os: str = client_info.get("os")
		self.client: str = client_info.get("client")


class PrivateChannel:
	def __init__(self, data: dict):
		self.data = data
		self.type: int = data.get("type")
		self.safety_warnings: list = data.get("safety_warnings", [])
		self.recipient_flags: int = data.get("recipient_flags")
		self.last_message_id: str = data.get("last_message_id")
		self.is_spam: bool = data.get("is_spam")
		self.is_message_request_timestamp: bool = data.get("is_message_request_timestamp")
		self.is_message_request: bool = data.get("is_message_request")
		self.id: str = data.get("id")
		self.flags: int = data.get("flags")
		self.recipients: list[User] = list()

		for recipient in data.get("recipients", []):
			self.recipients.append(User(recipient))


class Relationship:
	def __init__(self, data: dict):
		self.data: dict = data
		self.user_ignored: bool = data.get("user_ignored")
		self.type: int = data.get("type")
		self.since: str = data.get("since")
		self.nickname: str = data.get("nickname")
		self.is_spam_request: bool = data.get("is_spam_request")
		self.id: str = data.get("id")
		self.user = User(data.get("user"))



class UserSettings:
	def __init__(self, data: dict):
		self.data: dict = data


class AccountInfo:
	def __init__(self, data: dict):
		self.data: dict = data
		self.resume_gateway_url: str = data.get("resume_gateway_url")
		self.static_client_session_id: str = data.get("static_client_session_id")
		self.tutorial = data.get("tutorial")
		self.session_type: str = data.get("session_type")
		self.country_code: str = data.get("country_code")
		self.session_id: str = data.get("session_id")
		self.v: int = data.get("v")
		self.friend_suggestion_count: int = data.get("friend_suggestion_count")
		self.explicit_content_scan_version: int = data.get("explicit_content_scan_version")
		self.user_settings_proto: str = data.get("user_settings_proto")
		self.auth_session_id_hash: str = data.get("auth_session_id_hash")
		self.api_code_version: int = data.get("api_code_version")
		self.analytics_token: str = data.get("analytics_token")
		self.broadcaster_user_ids: list = data.get("broadcaster_user_ids", [])
		self._trace: list = data.get("_trace")
		self.guild_experiments: list = data.get("guild_experiments", [])
		self.experiments: list = data.get("experiments", [])
		self.connected_accounts: list[ConnectedAccount] = list()
		self.user: Profile = Profile(data.get("user", {}))
		self.sessions: list[Session] = list()
		self.geo_ordered_rtc_regions: list[str] = data.get("geo_ordered_rtc_regions", [])
		self.private_channels: list[PrivateChannel] = list()
		self.relationships: list[Relationship] = list()
		self.game_relationships: list = data.get("game_relationships", []) #idk
		
		
		self.guilds: list[dict] = data.get("guilds", [])
		self.presences: list[dict] = data.get("presences", [])
		self.experiments: list[dict] = data.get("experiments", [])
		self.read_state: list[dict] = data.get("read_state", [])
		self.notification_settings: dict = data.get("notification_settings", )
		self.guild_join_requests: list[dict] = data.get("guild_join_requests", [])
		self.auth: dict = data.get("auth")
		self.user_settings: UserSettings = UserSettings(data.get("user_settings", {}))
		self.notes: dict = data.get("notes")
		self.consents: dict = data.get("consents")
		self.user_guild_settings: list[dict] = data.get("user_guild_settings")


		for account in data.get("connected_accounts", []):
			self.connected_accounts.append(ConnectedAccount(account))
		
		for session in data.get("sessions", []):
			self.sessions.append(Session(session))

		for private_channel in data.get("private_channels", []):
			self.private_channels.append(PrivateChannel(private_channel))

		for relationship in data.get("relationships", []):
			self.relationships.append(Relationship(relationship))