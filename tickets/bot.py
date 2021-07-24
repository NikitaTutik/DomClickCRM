import requests
from django.conf import settings


def send_msg(text):
   token = settings.BOT_API_KEY
   chat_id = settings.BOT_CHAT_ID
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   send = requests.get(url_req)



