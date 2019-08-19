import requests
import pygal
import json
import math


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)

with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)

file_requests = req.json()
