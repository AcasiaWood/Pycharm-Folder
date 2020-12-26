from flask import Flask, render_template, request
import sqlite3
import cv2
import getpass
import smtplib
from email.mime.text import MIMEText
import pandas as pd
from utils.config import parse_args
from utils.data_loader import get_data_loader
from models.nk_model import nkModel

app = Flask(__name__)

conn = sqlite3.connect("account.db")
conn.execute("CREATE TABLE IF NOT EXISTS account (email TEXT, password TEXT)")
conn.close()


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
            msg['To'] = "eunandy09@naver.com"
            server = smtplib.SMTP_SSL("smtp.naver.com", 465)
            server.login(email, password)
            server.sendmail(email, "eunandy09@naver.com", msg.as_string())
            server.quit()
            conn = sqlite3.connect("account.db")
            cur = conn.cursor()
            cur.execute("select * from account")
            rows = cur.fetchall()
            signal = True
            for cols in rows:
                if email == cols[0]:
                    signal = False
                    break
            if signal:
                cur.execute("INSERT INTO account (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            conn.close()
            error = None
            return render_template('introduction.html', error=error)
        except (OSError, TypeError, UnicodeEncodeError):
            error = "The wrong account has been inputted."
            return render_template('introduction.html', error=error)
        except smtplib.SMTPAuthenticationError:
            error = "The account is not activated."
            return render_template('introduction.html', error=error)
    return render_template('introduction.html')


@app.route('/separation', methods=["GET", "POST"])
def separation():
    if request.method == "POST":
        try:
            cam = cv2.VideoCapture(0)
            while True:
                ret, frame = cam.read()
                if ret:
                    color = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
                    cv2.imshow('Camera', color)
                    q = cv2.waitKey(1) & 0xFF
                    if q == 27:
                        break
                    elif q == 13:
                        src = cv2.resize(color, dsize=(224, 224), interpolation=cv2.INTER_AREA)
                        cv2.imwrite("img/garbage.jpg", src)
                        break
                else:
                    raise cv2.error
            cam.release()
            cv2.destroyAllWindows()
            image = cv2.imread("img/garbage.jpg")
            cv2.imshow('Garbage', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            config = parse_args()
            separate(args=config)
            user = getpass.getuser()
            file = open("/home/{}/PycharmProjects/project/file/sample.csv".format(user), 'r')
            directory = file.readlines()
            if int(directory[1].strip('\n')) == 0:
                result = "Food Waste"
            else:
                result = "General Waste"
            return render_template('separation.html', result=result)
        except cv2.error:
            error = "An error has occurred while executing the camera system."
            return render_template('separation.html', error=error)
    return render_template('separation.html')


def separate(args):
    user = getpass.getuser()
    train_loader, test_loader = get_data_loader(args)
    model = nkModel(args, train_loader, test_loader)
    if args.is_train:
        model.train()
    else:
        temp_list = model.test()
        my_df = pd.DataFrame(temp_list)
        my_df.to_csv('/home/{}/PycharmProjects/project/file/sample.csv'.format(user), index=False, header=False)


if __name__ == '__main__':
    app.run()