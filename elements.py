class Element(object):
	def __init__(self, title, **kwargs):
		self.title = title
		allowed_args = ['subtitle', 'image_url', 'default_action', 'buttons']
		for k, v in kwargs.items():
			if k in allowed_args:
				setattr(self, k, v)
			else:
				raise TypeError("__init__() got an unexpected keyword argument '%s'" % k).tb_next

	def as_dict(self):
		temp = self.__dict__
		try:
			buttons = []
			for button in self.buttons:
				buttons.append(button.__dict__)
			temp['buttons'] = buttons
		except AttributeError:
			pass
		return temp