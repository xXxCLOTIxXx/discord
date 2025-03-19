

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
	MESSAGE_DELETE="MESSAGE_DELETE"
	MESSAGE_ACK="MESSAGE_ACK"
	INTERACTION_CREATE="INTERACTION_CREATE"
	USER_SETTINGS_PROTO_UPDATE="USER_SETTINGS_PROTO_UPDATE"
	SESSIONS_REPLACE="SESSIONS_REPLACE"
	PRESENCE_UPDATE="PRESENCE_UPDATE"
	GUILD_AUDIT_LOG_ENTRY_CREATE="GUILD_AUDIT_LOG_ENTRY_CREATE"
	FRIEND_REQUEST="RELATIONSHIP_ADD"
	DELETE_FRIEND="RELATIONSHIP_REMOVE"
	USER_NON_CHANNEL_ACK="USER_NON_CHANNEL_ACK"
	CALL_CREATE="CALL_CREATE"
	CALL_UPDATE="CALL_UPDATE"
	VOICE_STATE_UPDATE="VOICE_STATE_UPDATE"
	CALL_UPDATE="CALL_UPDATE"
	NOTIFICATION_CENTER_ITEMS_ACK="NOTIFICATION_CENTER_ITEMS_ACK"
	TYPING_START="TYPING_START"
	CONTENT_INVENTORY_INBOX_STALE="CONTENT_INVENTORY_INBOX_STALE"
	CHANNEL_UPDATE="CHANNEL_UPDATE"




class OPCODE:
	# Name                         Code  Client Action   Description
	DISPATCH =                     0  #  Receive         dispatches an event
	HEARTBEAT =                    1  #  Send/Receive    used for ping checking
	IDENTIFY =                     2  #  Send            used for client handshake
	PRESENCE_UPDATE =              3  #  Send            used to update the client status
	VOICE_STATE_UPDATE =           4  #  Send            used to join/move/leave voice channels
	VOICE_SERVER_PING =            5  #  Send            used for voice ping checking
	RESUME =                       6  #  Send            used to resume a closed connection
	RECONNECT =                    7  #  Receive         used to tell when to reconnect (sometimes...)
	REQUEST_GUILD_MEMBERS =        8  #  Send            used to request guild members (when searching for members in the search bar of a guild)
	INVALID_SESSION =              9  #  Receive         used to notify client they have an invalid session id
	HELLO =                        10 #  Receive         sent immediately after connecting, contains heartbeat and server debug information
	HEARTBEAT_ACK =                11 #  Sent            immediately following a client heartbeat that was received
	DM_UPDATE =                    13 #  Send            used to get dm features
	LAZY_REQUEST =                 14 #  Send            discord responds back with GUILD_MEMBER_LIST_UPDATE type SYNC...
	LOBBY_CONNECT =                15 #  ??
	LOBBY_DISCONNECT =             16 #  ??
	LOBBY_VOICE_STATES_UPDATE =    17 #  Receive
	STREAM_CREATE =                18 #  ??
	STREAM_DELETE =                19 #  ??
	STREAM_WATCH =                 20 #  ??
	STREAM_PING =                  21 #  Send
	STREAM_SET_PAUSED =            22 #  ??
	REQUEST_APPLICATION_COMMANDS = 24 #  Send            request application/bot cmds (user, message, and slash cmds)
