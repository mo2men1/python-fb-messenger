class Button(object):
	def __init__(self, button_type):
		self.type = button_type

class UrlButton(Button):
	def __init__(self, title, url, **kwargs):
		super().__init__("web_url")
		self.title = title
		self.url = url

		allowed_args = ['webview_height_ratio', 'messenger_extensions', 'fallback_url']
		for k, v in kwargs.items():
			if k in allowed_args:
				setattr(self, k, v)
			else:
				raise TypeError("__init__() got an unexpected keyword argument '%s'" % k).tb_next

class PostBackButton(Button):
	def __init__(self, title, payload):
		super().__init__("postback")
		self.title = title
		self.payload = payload

class LoginButton(Button):
	def __init__(self, url):
		super().__init__("account_link")
		self.url = url

class LogoutButton(Button):
	def __init__(self):
		super().__init__("account_unlink")

class ShareButton(Button):
	def __init__(self):
		super().__init__("element_share")