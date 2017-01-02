import json
import requests
from pprint import pprint
from .messages import TemplateMessage, Message, IncomingMessage
from .buttons import UrlButton
from .elements import Element
from .templates import ListTemplate, ButtonTemplate



class Messenger(object):
	"""docstring for Messenger"""
	def __init__(self, request, token):
		self.token = token
		if request['object'] == 'page':
			self.messages = []
			for entry in request['entry']:
				for msg in entry['messaging']:
					if 'message' in msg:
						mid = msg['message']['mid']
						seq = msg['message']['seq']
						sender = msg['sender']
						dic = msg['message']
						dic['sender'] = sender
						message = IncomingMessage(**dic)
						self.messages.append(message)

	def send(self, fbid, message):
		print("test")
		msg_data = {
	                  	"recipient": {
	                  		"id": fbid
	              		},
	              		"message": message.as_dict()
	      			}
		self.call_send_api(msg_data)

	# def seen(self, fbid):
	# 	msg_data = {
	# 		"recipient": {
	# 			"id": fbid
	# 		},
	# 		"sender_action": "mark_seen",
	# 		# "message": {},
	# 	}

		# self.call_send_api(msg_data)
		
	def call_send_api(self, msg_data):
		post_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + self.token
		post_msg = json.dumps(msg_data)
		status = requests.post(post_url, headers={"content-type": "application/json"}, data=post_msg)
		if status.status_code == 400:
			pprint(status.json())

