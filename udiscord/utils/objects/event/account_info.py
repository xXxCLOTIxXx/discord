

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


class Profile:
    def __init__(self, data: dict):
        self.data = data
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

         

        for account in data.get("connected_accounts", []):
            self.connected_accounts.append(ConnectedAccount(account))
        
        for session in data.get("sessions", []):
            self.sessions.append(Session(session))


        #TODO
        #private_channels
        #relationships
        #game_relationships
        #guilds
        #presences
        #experiments
        #read_state
        #notification_settings
        #guild_join_requests
        #auth
        #user_settings
        #notes
        #consents
        #user_guild_settings