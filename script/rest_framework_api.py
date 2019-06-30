import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"

get_endpoint = ENDPOINT + str(2)
data = json.dumps({"content": "Some random content"})

r = requests.get(get_endpoint)
print(r.text)

post_method = requests.post(ENDPOINT)
