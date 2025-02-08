
class Event:
    def __init__(self, data: dict, type: str = None):
        self.data: dict = data
        self.type: str | None = type