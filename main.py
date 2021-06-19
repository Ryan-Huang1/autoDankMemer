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

headers = {
    'authorization': os.getenv('authorization')
}

def apiCall():
    x = requests.post(url, data = data, headers=headers)
    print(x)

keep_alive()

while True:
    apiCall()
    number = randint(45, 100)
    print(number)
    time.sleep(number)