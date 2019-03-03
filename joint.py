

import requests
import os

payload = {
        'username': os.environ['USERNAME'],
        'password': os.environ['PASSWORD']
}
resp = requests.post('https://portal-sso-develop.iii-cflab.com/v2.0/auth/native', json=payload)


header = {
        "content-type": "application/json",
        "Authorization": "Bearer " + resp.json()['accessToken']
}
resp = requests.get("https://api-afs-develop.iii-cflab.com/v2/instances", headers=header)
print(resp2.json())
