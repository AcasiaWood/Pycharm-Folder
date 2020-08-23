import requests

client_id = "privacy"
client_secret = "privacy"

url = "https://openapi.naver.com/v1/vision/celebrity"

files = {'image': open('sample.jpg', 'rb')}
headers = {'X-Naver-Client-ID': client_id, 'X-Naver-Client-Secret': client_secret}
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error Code:" + rescode)
