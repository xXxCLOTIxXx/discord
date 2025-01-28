from . import UserProfile

class Event:
    def __init__(self, data: dict, type: str = None):
        self.data: dict = data
        self.type: str | None = type
        self.author: UserProfile = UserProfile(data.get("author", {}))