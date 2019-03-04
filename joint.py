

import requests
import os

WISE_PAAS_INSTANCE = 'iii-cflab.com'
ENDPOINT_SSO = 'portal-sso-develop'
ENDPOINT_AFS = 'api-afs-develop'
ENDPOINT_APM = ''

payload = dict()
payload['username'] = os.environ['USERNAME']
payload['password'] = os.environ['PASSWORD']
resp = requests.post('https://' + ENDPOINT_SSO + '.' + WISE_PAAS_INSTANCE + '/v2.0/auth/native', 
                     json=payload,
                     verify=False)

header = dict()
header['content-type'] = 'application/json'
header['Authorization'] = 'Bearer ' + resp.json()['accessToken']
resp = requests.get('https://' + ENDPOINT_AFS + '.' + WISE_PAAS_INSTANCE + '/v2/instances', 
                    headers=header,
                    verify=False)
print(resp.json())


ENDPOINT_APM = 'api-apm-acniotsense-apmdemo'
APM_HIST = 'https://' + ENDPOINT_APM + '.' + WISE_PAAS_INSTANCE + '/hist/raw/data'

payload = dict()
payload['nodeId'] = '272'
payload['sensorType'] = 'monitor'
payload['sensorName'] = 'cnc_predict'
payload['startTs'] = '2018-12-29T00:36:18.000Z'
payload['endTs'] = '2018-12-30T00:36:58.000Z'

header = dict()
header['content-type'] = 'application/json'
header['Authorization'] = 'Bearer ' + resp.json()['accessToken']

r = requests.get(APM_HIST, 
                 params=payload, 
                 headers=header,
                 verify=False)
print(r.url)
