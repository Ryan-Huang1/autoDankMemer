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

auth3 = {
    'authorization': os.getenv('auth3')
}

auth4 = {
    'authorization': os.getenv('auth4')
}

def apiCall():
    account1 = requests.post(url, data = data, headers=auth1)
    print(f'account1 {account1}')
    account2 = requests.post(url, data = data, headers=auth2)
    print(f'account2 {account2}')
    account3 = requests.post(url, data = data, headers=auth3)
    print(f'account3 {account3}')
    account4 = requests.post(url, data = data, headers=auth4)
    print(f'account4 {account4}')

keep_alive()

while True:
    apiCall()
    number = randint(45, 100)
    print(number)
    time.sleep(number)