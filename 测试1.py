import requests
import json

data = {
    'a':123,
    'b':456
}

headers = {'Content-Type':'application/json'}

response = requests.post(url= '',headers=headers,data=json.dumps(data))

