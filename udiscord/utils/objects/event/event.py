
class Event:
    def __init__(self, data: dict, type: str = None, op: int = None):
        self.data: dict = data
        self.type: str | None = type
        self.OPCODE: int | None = op