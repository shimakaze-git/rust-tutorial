from requests.auth import HTTPBasicAuth
import requests


url = "https://komoju.com/api/v1/payments"
user = ""

req = requests.get(url, auth=HTTPBasicAuth(user, ''))
# print(req)

# print(dir(req))
# print(req.text)

payload = {
    'amount': 100,
    'currency': "test",
    'external_order_num': 100
}

print(len(payload))

for i in payload:
    print(i)
# test['test10'] = 100
# print(test)