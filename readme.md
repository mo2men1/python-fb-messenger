# Example Django View

Please refer to the Facebook messenger platform [documentation](https://developers.facebook.com/docs/messenger-platform)

This is an example Django view to demonstrate the basic functions implemented by this library.

You can use [ngrok](https://ngrok.com/) to tunnel your localhost into https url.

you need to add the Facebook page access token to your settings file like this:
```python
FB_PAGE_ACCESS_TOKEN = "EAALJX..."

```
or send the token to Messenger module constructor directly.
```python
	req = json.loads(request.body.decode('utf-8'))
	messenger = Messenger(req, "EAALJX...")
```

views.py:

```python
from django.views import generic
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from pprint import pprint
from .fb_messenger.messenger import Messenger
from .fb_messenger.messages import TextMessage
from .fb_messenger.templates import ButtonTemplate, GenericTemplate, ListTemplate
from .fb_messenger.buttons import UrlButton, PostBackButton, ShareButton, LoginButton, LogoutButton
from .fb_messenger.elements import Element
# Create your views here.

class TestingBot(generic.View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request):
		return generic.View.dispatch(self, request)

	def get(self, request):
		if request.GET['hub.verify_token'] == '8787':
			return HttpResponse(request.GET['hub.challenge'])
		return HttpResponse("Error, invalid token")

	def post(self, request):
		req = json.loads(request.body.decode('utf-8'))
		pprint(req)
		token = settings.FB_PAGE_ACCESS_TOKEN
		messenger = Messenger(req, token)
		msgs = messenger.messages
		for msg in msgs:
			sender = msg.sender['id']
			messenger.sender_action(fbid=sender, type="mark_seen")
			messenger.sender_action(fbid=sender, type="typing_on")
			if msg.text:
				e1 = Element(title="ACES Expo", subtitle="Apply now for ACES Expo.", image_url="https://scontent-cai1-1.xx.fbcdn.net/v/t1.0-9/15203360_1318481058204029_485154955656869307_n.png?oh=eebc8f1fdc1cc97f62f431606dfaa4cc&oe=59249794")
				e2 = Element(title="Dell EMC", subtitle="Apply for Dell EMC.", image_url="https://acesegypt.org/media/images/companies/Dell.png")
				e3 = Element(title="ITWORX", subtitle="Apply for ITWORX.", image_url="https://acesegypt.org/media/images/companies/Copy_of_1610908_10153133566040236_1066194039882429794_n_1.png")

				if msg.text.lower() == "list":
					Expo_button = UrlButton(title="Apply Now", url="www.acesegypt.org/Expo", webview_height_ratio="tall")
					apply_button = UrlButton(title="Apply", url="www.acesegypt.org", webview_height_ratio="tall")
					more_button = UrlButton(title="View More", url="www.acesegypt.org/Expo", webview_height_ratio="tall")
					default = more_button.as_dict()
					default.pop("title")

					e1.buttons = [Expo_button]
					e1.default_action = default

					e2.buttons = [apply_button]
					e2.default_action = default

					e3.buttons = [apply_button]
					e3.default_action = default

					message = ListTemplate(elements=[e1, e2, e3], buttons=[more_button])

				elif msg.text.lower() == "button":
					yes_button = PostBackButton(title="Yes", payload="YES")
					no_button = PostBackButton(title="No", payload="NO")
					message = ButtonTemplate(text="Did you like our event?", buttons=[yes_button, no_button])

				elif msg.text.lower() == "generic":
					apply_button = UrlButton(title="Apply", url="www.acesegypt.org", webview_height_ratio="tall")
					e1.buttons = [apply_button]
					e2.buttons = [apply_button]
					e3.buttons = [apply_button]
					message = GenericTemplate([e1, e2, e3])

				elif msg.text.lower() == "login":
					login_button = LoginButton(url="https://acesegypt.org")
					message = ButtonTemplate(text="Welcome to ACES Egypt", buttons=[login_button])
					
				else:
					text = "Thanks, we will get back to you soon."
					message = TextMessage(text)

				messenger.send(fbid=sender, message=message)

		return HttpResponse()

```