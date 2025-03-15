


class Guilds:
	def __init__(self, data: list = []):
		self.data = data
		self.size = len(self.data)
		self.guilds: list[Guild] = list()
		for guild in self.data:
			self.guilds.append(Guild(guild))


class Guild:
	def __init__(self, data: dict = {}):
		self.data = data
		self.guildId = self.data.get("id")
		self.guildName = self.data.get("name")
		self.icon = self.data.get("icon")
		self.owner = self.data.get("owner")
		self.permissions = self.data.get("permissions")
		self.features = self.data.get("features", [])