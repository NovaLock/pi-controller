#!/usr/bin/python

import json
import requests


server_addr = "http://127.0.0.1:3000"
init_data = {
  "version": "Prometheus/1.0",
  "function": "init_server",
  "parameters": []
}

init_data_json = json.dumps(init_data)

headers = {'Content-type': 'application/json'}

print init_data_json

init_response = requests.post(server_addr, data=init_data_json, headers=headers)

print init_response.content

dec_init_response = json.loads(init_response.content)

token = dec_init_response['result']


print token



