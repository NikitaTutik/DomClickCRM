import requests
from django.conf import settings


def send_msg(text):
   token = '1842995007:AAGgpe5ivziqOy5DLWJNx41Euq1Xfq6rjJ8'
   chat_id = "-583457919"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   send = requests.get(url_req)



