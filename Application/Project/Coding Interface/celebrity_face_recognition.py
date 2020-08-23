import requests

client_id = "No ID was entered to protect personal information."
client_secret = "No password was entered to protect personal information."

url = "https://openapi.naver.com/v1/vision/celebrity"

files = {'image': open('sample.png', 'rb')}
headers = {'X-Naver-Client-ID': client_id, 'X-Naver-Client-Secret': client_secret}
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error Code:" + rescode)
