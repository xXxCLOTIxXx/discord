from .. import log
from ..utils.objects import AccountInfo, Event, Message, EventType
from traceback import format_exc

class Handler:
    handlers: dict = {}

    def handle_data(self, _data: dict):
        t = _data.get('t')
        op = _data.get('op')
        s = _data.get('s')
        data = _data.get('d')
        log.debug(f"[socket][received]: t: {t} op: {op} s: {s}")
        if t:
            self.call(data, t)

    def call(self, data: dict, type: str):
        if type in self.handlers or EventType.ANY in self.handlers:
            match type:
                case EventType.READY:
                    data = AccountInfo(data)
                case EventType.MESSAGE_CREATE:
                    data = Message(data)
                case EventType.MESSAGE_UPDATE:
                    data = Message(data)
                case _:
                    data = Event(data, type)
            for i in (EventType.ANY, type):
                if i not in self.handlers:
                    continue
                for func in self.handlers[i]:
                    try:
                        if i == EventType.ANY:
                            func(data, type)
                        else:
                            func(data)
                    except Exception as e:
                        log.error(f"[event][{func}]Error: {e}{'' if not self.detailed_error else f'\n{format_exc()}'}")

    def event(self, type: str):
        """
        Decorator for registering an event handler.

        :param type: Event type string or udiscord.EventType.ANY.
        :return: Decorator function.
        """
        def registerHandler(handler):
            self.add_handler(type, handler)
            return handler
        return registerHandler

    def add_handler(self, type: str, handler):
        """
        Registers an event handler for a specific event type.

        :param type: Event type string or udiscord.EventType.ANY.
        :param handler: Function to handle the event.
        :return: The registered handler.
        """
        if type in self.handlers:
            self.handlers[type].append(handler)
        else:
            self.handlers[type] = [handler]
        return handler

    @staticmethod
    def command_validator(commands: list, handler):
        def wrapped_handler(data):
            if not isinstance(data.content, str):
                return
            
            message_content = data.content.lower()
            for command in commands:
                if message_content.startswith(command.lower()):
                    data.content = data.content[len(command):].strip()
                    handler(data)
                    break
        return wrapped_handler

    def command(self, commands: list):
        """
        Decorator for registering a command handler.

        :param commands: List of commands.
        :return: Decorator function.
        """
        def registerCommands(handler):
            self.add_command(commands, handler)
            return handler
        return registerCommands

    def add_command(self, commands: list, handler):
        """
        Registers a command handler for processing messages.

        :param commands: List of commands.
        :param handler: Function to execute when a command is detected.
        :return: Command validator function.
        """
        if EventType.MESSAGE_CREATE in self.handlers:
            self.handlers[EventType.MESSAGE_CREATE].append(self.command_validator(commands, handler))
        else:
            self.handlers[EventType.MESSAGE_CREATE] = [self.command_validator(commands, handler)]
        return self.command_validator
