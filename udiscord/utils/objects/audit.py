

class AuditLog:
	def __init__(self, data: dict):
		self.data = data
		self.audit_log_entries = data.get("audit_log_entries", [])
		self.users = data.get("users", [])
		self.integrations = data.get("integrations", [])
		self.webhooks = data.get("webhooks", [])
		self.guild_scheduled_events = data.get("guild_scheduled_events", [])
		self.threads = data.get("threads", [])
		self.application_commands = data.get("application_commands", [])
		self.auto_moderation_rules = data.get("auto_moderation_rules", [])
