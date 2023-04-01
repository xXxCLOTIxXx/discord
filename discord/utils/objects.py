


class LoginInfo:
	def __init__(self, data: dict = {}):
		self.json = data
		user_settings = self.json.get("user_settings")
		
		self.token = self.json.get("token")
		self.user_id = self.json.get("user_id")
		self.locale = user_settings.get("locale")
		self.theme = user_settings.get("theme")