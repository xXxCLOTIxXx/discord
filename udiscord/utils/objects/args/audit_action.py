

class AuditAction:
    """
    A class for conveniently specifying action filters in the audit log.

    This class contains a set of constants representing various types of actions 
    in the audit log. It is used for filtering records when calling `client.get_audit_logs`.

    Usage examples:
        logs = client.get_audit_logs(action_type=AuditAction.CreateChannel)
        logs = client.get_audit_logs(action_type=AuditAction.DeleteMember)
    
    """
    AllActions = None
    CreateChannel: int = 10
    ServerUpdate: int = 1
    ChannelUpdate: int = 11
    DeleteChannel: int = 12
    CreateChannelRights: int = 13
    ChangeChannelRights: int = 14
    DeleteChannelRights: int = 15
    DeleteMember: int = 20

    #there are many more types of actions in the audit log... I'll add them all a bit later...