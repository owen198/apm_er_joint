

import requests

url = "https://portal-sso-develop.iii-cflab.com/v2.0/auth/native"
payload = {
        'username': "dev@gmail.com",
        'password': "password"
}

resp = requests.post(url, json=payload)


header2 = {
        "content-type": "application/json",
        "Authorization": "Bearer " + resp.json()['accessToken']
}

resp2 = requests.get("https://api-afs-develop.iii-cflab.com/v2/instances", headers=header2)
print(resp2.json())
