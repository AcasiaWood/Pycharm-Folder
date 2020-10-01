from flask import Flask, render_template, redirect, request, url_for
import urllib.request
import json
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/introduction', methods=["GET", "POST"])
def introduction():
    if request.method == "POST":
        text = request.form.get('text')
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            msg = MIMEText(text, _charset='euc-kr')
            msg['Subject'] = "{}-Feedback".format(email)
            msg['From'] = email
            msg['To'] = "private"
            server = smtplib.SMTP_SSL("smtp.naver.com", 465)
            server.login(email, password)
            server.sendmail(email, "private", msg.as_string())
            server.quit()
        except:
            pass
    return render_template('introduction.html')

@app.route('/translation', methods=["GET", "POST"])
def translation():
    if request.method == "POST":
        client_id = "private"
        client_secret = "private"

        language = ["ko", "ja", "zh-cn", "zh-tw", "hi", "en", "es", "fr", "de", "pt", "vi", "id", "fa", "ar", "mm",
                    "th", "ru", "it"]

        text = request.form.get('text')
        src = request.form.get('source')
        tar = request.form.get('target')

        if src != tar:
            try:
                if src in language and tar in language:
                    encText = urllib.parse.quote(text)
                    data = "source=" + src + "&target=" + tar + "&text=" + encText
                    url = "https://openapi.naver.com/v1/papago/n2mt"
                    claim = urllib.request.Request(url)
                    claim.add_header("X-Naver-Client-Id", client_id)
                    claim.add_header("X-Naver-Client-Secret", client_secret)

                    response = urllib.request.urlopen(claim, data=data.encode("utf-8"))
                    rescode = response.getcode()

                    if rescode == 200:
                        response_body = response.read()
                        res = json.loads(response_body.decode('utf-8'))
                        from pprint import pprint
                        pprint(res)
                        return render_template('translation.html', text=res['message']['result']['translatedText'])
                    else:
                        print("Error Code: " + rescode)
                else:
                    error = "The departure language and arrival language have not been entered."
                    return render_template('translation.html', error=error)
            except urllib.error.HTTPError:
                error = "No text has been entered."
                return render_template('translation.html', error=error)
        elif src == "" and tar == "":
            error = "The departure language and arrival language have not been entered."
            return render_template('translation.html', error=error)
        else:
            error = "The departure language and arrival language are same."
            return render_template('translation.html', error=error)
    return render_template('translation.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
