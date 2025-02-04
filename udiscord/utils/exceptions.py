from json import loads

class WrongModeError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

#=====================================================

class UnknownError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class RateLimited(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


class InsufficientRights(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class InvalidLoginOrPassword(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


class InvalidAuthorizationToken(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class IncorrectJsonData(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class IncorrectJsonData(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class UnknownInvitation(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class IncorrectServer(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class IncorrectServer(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


errors = {
	20028: RateLimited,
	40062: RateLimited,
	50013: InsufficientRights,
	50035: InvalidLoginOrPassword,
	50109: IncorrectJsonData,
	10006: UnknownInvitation,
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