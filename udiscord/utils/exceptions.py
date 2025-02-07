from json import loads

class DiscordError(Exception):
    """
    Base class for all Discord-related errors.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


class LibraryError(Exception):
    """
    Base class for all library-related errors.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)
#++++++++++++++++++++++++++++++++++++++++++++++++++++=



class WrongModeError(LibraryError):
    """
    An incorrect or unexpected mode is set.
    """


class ArgumentNotSpecifiedError(LibraryError):
    """
    A required argument was not provided.
    """


class UnauthorizedClientError(LibraryError):
    """
    The client is not authorized to perform this action.
    """


class UnknownError(LibraryError):
    """
    An unknown error occurred.
    """

#=====================================================


class RateLimited(DiscordError):
    """
    Too many requests have been sent in a short period.
    """


class InsufficientRights(DiscordError):
    """
    The user does not have the necessary permissions to perform this action.
    """


class InvalidLoginOrPassword(DiscordError):
    """
    The provided login or password is incorrect.
    """


class InvalidAuthorizationToken(DiscordError):
    """
    The provided authorization token is invalid or expired.
    """


class IncorrectJsonData(DiscordError):
    """
    The provided JSON data is malformed or contains invalid values.
    """


class UnknownInvitation(DiscordError):
    """
    The specified invitation code is invalid or does not exist.
    """


class IncorrectServer(DiscordError):
    """
    The specified server does not exist or cannot be accessed.
    """


class USERNAME_BLOCKED_UNVERIFIED(DiscordError):
    """
    The username is blocked due to the account being unverified.
    """


errors = {
	20028: RateLimited,
	40062: RateLimited,
	50013: InsufficientRights,
	50035: InvalidLoginOrPassword,
	50109: IncorrectJsonData,
	10006: UnknownInvitation,
	50035: USERNAME_BLOCKED_UNVERIFIED,
	50055: IncorrectServer
}

def checkException(data):
	try:
		data = loads(data)
		code = data["code"]
	except:
		raise UnknownError(data)
	if code in errors: raise errors[code](data)
	else:raise UnknownError(data)