from keep_alive import keep_alive
from random import randint
import requests
import time
import os

url = 'https://discord.com/api/v9/channels/855820738653323267/messages'

data = {
    'content': 'pls beg',
    'tts': False
}

auth1 = {
    'authorization': os.getenv('auth1')
}

auth2 = {
    'authorization': os.getenv('auth2')
}

def apiCall():
    account1 = requests.post(url, data = data, headers=auth1)
    print(account1)
    account2 = requests.post(url, data = data, headers=auth2)
    print(account2)

keep_alive()

while True:
    apiCall()
    number = randint(45, 100)
    print(number)
    time.sleep(number)