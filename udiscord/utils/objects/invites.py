from . import UserProfile, Guild, Channel

class Invites:
    def __init__(self, data: list):
        self.data: dict = data
        self.size: int = len(data)
        self.invites: list[Invite] = list()
        for i in data:
            self.invites.append(
                Invite(i)
            )



class Invite:
    def __init__(self, data: dict):
        self.data: dict = data
        self.type: int = data.get('type')
        self.code: str = data.get('code')
        self.inviter: UserProfile = UserProfile(data.get("inviter", {}))
        self.max_age: int = data.get("max_age")
        self.created_at: str = data.get("created_at")
        self.expires_at = data.get("expires_at")
        self.flags: int = data.get("flags")
        self.guild: Guild = Guild(data.get("guild", {}))
        self.guild_id: str = data.get("guild_id")
        self.channel: Channel = Channel(data.get("channel", {}))
        self.uses: int = data.get("uses")
        self.max_uses: int = data.get("max_uses")
        self.temporary: bool = data.get("temporary")
        self.approximate_member_count: int = data.get("approximate_member_count")
        self.approximate_presence_count: int = data.get("approximate_presence_count")