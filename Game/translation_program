import urllib.request
import json

client_id = "No ID was entered to protect personal information."
client_secret = "No password was entered to protect personal information."

language = ["ko", "ja", "zh-cn", "zh-tw", "hi", "en", "es", "fr", "de", "pt", "vi", "id", "fa", "ar", "mm", "th", "ru", "it"]

# import notepad to translate (txt format)

with open('source.txt', 'r', encoding='utf8') as f:
    srcText = f.read()

enter = input("Enter the Language : ")

for i in range(0, len(language)):
    if language[i] == enter:
        print("Language Check Completed")

# stored in the encText variable, the notepad language is Korean, and the language to be translated is English.

encText = urllib.parse.quote(srcText)
data = "source=ko&target="+enter+"&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# data encryption, check whether the import is correct or not

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()

    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    pprint(res)

    with open('translate.txt', 'w', encoding='utf8') as f:
        f.write(res['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)
