from messages import TemplateMessage

class ButtonTemplate(TemplateMessage):
	def __init__(self, text, buttons):
		super().__init__("button")
		self.text = text
		self.buttons = buttons

	def as_dict(self):
		temp = super().as_dict()
		buttons = []
		for button in self.buttons:
			buttons.append(button.__dict__)
		temp['attachment']['payload']['buttons'] = buttons
		return temp

class GenericTemplate(TemplateMessage):
	def __init__(self, elements):
		super().__init__("generic")
		self.elements = elements

	def as_dict(self):
		temp = super().as_dict()
		elements = []
		for element in self.elements:
			elements.append(element.as_dict())
		temp['attachment']['payload']['elements'] = elements
		return temp

class ListTemplate(TemplateMessage):
	def __init__(self, elements, buttons=[], cover=True):
		super().__init__("list")
		self.top_element_style = "large" if cover else "compact"
		self.elements = elements
		self.buttons = buttons

	def as_dict(self):
		temp = super().as_dict()
		elements = []
		for element in self.elements:
			elements.append(element.as_dict())
		temp['attachment']['payload']['elements'] = elements
		return temp