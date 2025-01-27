from .. import Event, log


class Handler:
	handlers: dict = {}
	
	def handle_data(self, _data: dict):
		t = _data.get('t')
		op = _data.get('op')
		s = _data.get('s')
		data = _data.get('d')
		log.debug(f"[ws][message]: t:{t}\nop: {op}\n s: {s}")
		if t:self.call(data, t)

	def call(self, data: dict, type: str):
		data = Event(data, type)
		if type in self.handlers.keys():
			for func in self.handlers[type]:
				try:func(data)
				except Exception as e:
					log.error(f"[event][{func}]Error: {e}")

	def event(self, type: str):
		def registerHandler(handler):
			self.add_handler(type, handler)
			return handler
		return registerHandler


	def add_handler(self, type: str, handler):
			if type in self.handlers:self.handlers[type].append(handler)
			else:self.handlers[type] = [handler]
			return handler