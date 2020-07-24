import time
import hashlib
import hmac
import requests
import json

api_key = ''
api_secret = ''

url = 'https://api.tdax.com/api/orders/'

#EXAMPLE CREATE ORDER DATA
amount = 0.1
price = 6
nonce = int(time.time())
side = 'buy'
pair = 'algo_thb'

req_header = 'amount='+str(amount)+'&nonce='+str(nonce)+'&pair='+str(pair)+'&price='+str(price)+'&side='+str(side)+'&type=limit'

hasher = hmac.new(api_secret, req_header, digestmod=hashlib.sha512).hexdigest()

payload = {
    'type':'limit',
    'pair':'algo_thb',
    'side':'buy',
    'nonce':nonce,
    'price':'6',
    'amount':'0.1'
}

header = {
    'content-type':'application/json',
    'Authorization':'TDAX-API '+api_key,
    'Signature':hasher
}

res = requests.post(url, data=json.dumps(payload), headers=header)

print(res)



