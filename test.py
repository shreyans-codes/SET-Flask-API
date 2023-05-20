import requests
BASE = "http://127.0.0.1:5000/"
response1 = requests.get(
    BASE + "/parameters/30.21/30.54/40.2/35.011/12.79/8.7/25.32")
print(response1.json())

# from crop_recommend import apiCallFunction

# retVal = apiCallFunction(N=104, P=33, K=32, temp=23.00,
#                          humidity=66.00, ph=6.22, rainfall=140.000)
# print(retVal)
