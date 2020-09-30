import urllib.request
import json

client_id = "privacy"
client_secret = "privacy"

language = ["ko", "ja", "zh-cn", "zh-tw", "hi", "en", "es", "fr", "de", "pt", "vi", "id", "fa", "ar", "mm", "th", "ru", "it"]

with open('source.txt', 'r', encoding='utf8') as file:
    srcText = file.read()

print("Language: {}".format(language))
src = input("Language: ")
tar = input("Language: ")

encText = urllib.parse.quote(srcText)
data = "source=" + src + "&target=" + tar + "&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()

    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    pprint(res)

    with open('translation.txt', 'w', encoding='utf8') as file:
        file.write(res['message']['result']['translatedText'])
else:
    print("Error Code: " + rescode)
