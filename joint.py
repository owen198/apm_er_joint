

import requests
import os

WISE_PAAS_INSTANCE = 'iii-cflab.com'
ENDPOINT_SSO = 'portal-sso-develop'
ENDPOINT_AFS = 'api-afs-develop'

payload = {
        'username': os.environ['USERNAME'],
        'password': os.environ['PASSWORD']
}
resp = requests.post('https://' + ENDPOINT_SSO + '.' + WISE_PAAS_INSTANCE + '/v2.0/auth/native', 
                     json=payload,
                     verify=False)


header = {
        "content-type": "application/json",
        "Authorization": "Bearer " + resp.json()['accessToken']
}
resp = requests.get('https://' + ENDPOINT_AFS + '.' + WISE_PAAS_INSTANCE + '/v2/instances', 
                    headers=header,
                    verify=False)
print(resp.json())
