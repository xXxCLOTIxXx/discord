from json import loads

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



errors = {
	40062: RateLimited,
	50013: InsufficientRights,
	50035: InvalidLoginOrPassword
}

def checkException(data):
	try:
		data = loads(data)
		code = data["code"]
	except:
		raise UnknownError(data)
	if code in errors: raise errors[code](data)
	else:raise UnknownError(data)