import os
import sys
import requests

client_id = "여기를 지우고 클라이언트 아이디를 넣으세요."
client_secret = "여기를 지우고 클라이언트 시크릿을 넣으세요."

url = "https://openapi.naver.com/v1/vision/celebrity"

files = {'image': open('여기를 지우고 확장자를 포함한 파일 이름을 넣으세요.', 'rb')}
headers = {'X-Naver-Client-ID': client_id, 'X-Naver-Client-Secret': client_secret}
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error Code:" + rescode)
