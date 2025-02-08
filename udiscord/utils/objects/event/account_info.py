

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


        #TODO
        #broadcaster_user_ids
        #private_channels
        #_trace
        #guild_experiments
        #relationships
        #game_relationships
        #presences
        #experiments
        #connected_accounts
        #user
        #read_state
        #notification_settings
        #guild_join_requests
        #auth
        #user_settings
        #notes
        #guilds
        #sessions
        #geo_ordered_rtc_regions
        #consents
        #user_guild_settings