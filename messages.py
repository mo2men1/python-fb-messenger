from  abc import ABC, abstractmethod
from collections import namedtuple

class Message(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def as_dict(self):
		pass

class TextMessage(Message):
	def __init__(self, text):
		# super().__init_)
		self.text = text

	def as_dict(self):
		return {"text": self.text}

class TemplateMessage(Message, ABC):
	@abstractmethod
	def __init__(self, template_type):
		# super().__init_()
		self.template_type = template_type

	@abstractmethod
	def as_dict(self):
		return {
			"attachment": {
				"type": "template",
				"payload": 	self.__dict__
			}
		}

IncomingMessage = namedtuple('IncomingMessage', ['sender', 'mid', 'seq', 'text', 'attachments', 'sticker_id'])
IncomingMessage.__new__.__defaults__ = (None,) * 4