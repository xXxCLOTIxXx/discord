

class EventType:
    """
    A class containing constant event types for use with event handling.

    These event types represent various events that can be received or handled
    from the Discord WebSocket API. They are used to identify the type of event
    that is triggered, such as user updates, messages, interactions, and more.
    """
    ANY = "ANY"
    READY="READY"
    PRESENCE_UPDATE="PRESENCE_UPDATE"
    MESSAGE_CREATE="MESSAGE_CREATE"
    MESSAGE_UPDATE="MESSAGE_UPDATE"
    MESSAGE_ACK="MESSAGE_ACK"
    INTERACTION_CREATE="INTERACTION_CREATE"
    USER_SETTINGS_PROTO_UPDATE="USER_SETTINGS_PROTO_UPDATE"