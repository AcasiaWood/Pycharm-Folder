import sqlite3
import requests
import json
import os
import webbrowser
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename

conn = sqlite3.connect("shopping_database.db")
print("opened database successfully")
conn.execute("CREATE TABLE IF NOT EXISTS SHOPPING (item TEXT, num TEXT, price TEXT)")
print("table created successfully")

conn = sqlite3.connect("account_database.db")
print("opened database successfully")
conn.execute("CREATE TABLE IF NOT EXISTS LOGIN (email TEXT, password TEXT, money TEXT)")
print("table created successfully")

email, password = map(str, input('enter your email and password to confirm your information: ').split())

if email == 'admin' and password == '123456':
    conn = sqlite3.connect("shopping_database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()

    select = str(input('whether to delete export database (y/n): '))

    if select == 'y':
        if len(rows) != 0:
            conn.execute("DELETE FROM shopping")
            conn.commit()
            print("table deleted successfully")
        else:
            print("error: there are no entries in table.")
    else:
        print("table deleted unsuccessfully")

    conn.close()

    conn = sqlite3.connect("account_database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from login")
    rows = cur.fetchall()

    select = str(input('whether to delete account database (y/n): '))

    if select == 'y':
        if len(rows) != 0:
            conn.execute("DELETE FROM login")
            conn.commit()
            print("table deleted successfully")
        else:
            print("error: there are no entries in table.")
    else:
        print("table deleted unsuccessfully")

conn = sqlite3.connect("account_database.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("INSERT INTO login (email, password, money) VALUES (?, ?, ?)", ('admin', '123456', 10000))
conn.commit()
conn.close()

app = Flask(__name__)

app.secret_key = 'admin'


@app.route('/')
def default_setting():
    return render_template('localhost.html')


def account_info():
    account = {}
    log_conn = sqlite3.connect('account_database.db')
    log_conn.row_factory = sqlite3.Row
    log_cur = log_conn.cursor()
    log_cur.execute("select * from login")
    log_rows = log_cur.fetchall()
    for log_row in log_rows:
        account[log_row[0]] = log_row[1]
    log_conn.close()
    return account, render_template("account.html", rows=rows)


def check_out(email, password):
    flag = False
    account, _ = account_info()
    try:
        if account[email] == password:
            flag = True
    except KeyError:
        flag = False
    return flag


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    flag = True
    if not session.get('logged_in'):
        if request.method == "POST":
            log_email, log_password = request.form['email'], request.form['password']
            if log_email == '':
                error = ' email contains invalid special characters.'
                return render_template('register.html', error=error)
            else:
                log_conn = sqlite3.connect('account_database.db')
                log_conn.row_factory = sqlite3.Row
                log_cur = log_conn.cursor()
                log_cur.execute("select * from login")
                log_rows = log_cur.fetchall()
                for log_row in log_rows:
                    if log_row[0] == log_email:
                        flag = False
                        break
                if not flag:
                    error = ' email already exists, try to register again.'
                    log_conn.close()
                else:
                    session['logged_in'] = True
                    log_cur.execute("INSERT INTO login (email, password, money) VALUES (?, ?, ?)",
                                    (email, password, 10000))
                    log_conn.commit()
                    log_conn.close()
                    return redirect(url_for('homepage'))
    else:
        logout()
    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if not session.get('logged_in'):
        if request.method == 'POST':
            check = check_out(request.form['email'], request.form['password'])
            if not check:
                error = ' invalid account, try to login again.'
            else:
                session['logged_in'] = True
                return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return default_setting()


def analysis(route):
    error = None

    client_id = "private"
    client_secret = "private"

    url = "https://openapi.naver.com/v1/vision/celebrity"

    try:
        img = route
        files = {'image': open(img, 'rb')}
        headers = {'X-Naver-Client-ID': client_id, 'X-Naver-Client-Secret': client_secret}
        response = requests.post(url, files=files, headers=headers)
        rescode = response.status_code
    except FileNotFoundError:
        response = None
        rescode = 400
        error = True

    if rescode == 200:
        print(response.text)
    else:
        print("Error Code:" + str(rescode))

    try:
        return error, json.loads(response.text)["faces"][0]["celebrity"]["confidence"]
    except (AttributeError, KeyError):
        return error, False


def compare_file(route):
    error, record = analysis(route=route)
    system = False
    permission = {'permit': 0, 'refuse': None}
    if not permission or error:
        system = False
        return system
    else:
        for data in permission.values():
            try:
                if data < record < data + 1:
                    system = True
                    return system
            except TypeError:
                break
        return system


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        route = 'analysis/' + secure_filename(file.filename)
        print(route)
        try:
            file.save('analysis/' + secure_filename(file.filename))
            system = compare_file(route=route)
            os.remove(route)
            if system:
                return redirect(url_for('homepage'))
            else:
                return render_template('upload.html')
        except (FileNotFoundError, IsADirectoryError, PermissionError):
            return render_template('upload.html')
    return render_template('upload.html')


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        url = request.form['search']
        webbrowser.open(url=url)
    return render_template('homepage.html')


@app.route('/information', methods=['GET', 'POST'])
def information():
    global email, password, balance
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        check = check_out(email, password)
        if not check:
            error = ' invalid account, try to login again.'
        else:
            log_conn = sqlite3.connect("account_database.db")
            log_conn.row_factory = sqlite3.Row
            log_cur = log_conn.cursor()
            log_cur.execute("select * from login")
            log_rows = log_cur.fetchall()
            for log_row in log_rows:
                if log_row[0] == email:
                    balance = log_row[2]
                    return render_template('information.html', email=email, password=password, balance=balance)
    return render_template('authentication.html', error=error)


@app.route('/notice', methods=['GET', 'POST'])
def notice():
    return render_template("notice.html")


@app.route('/charge_balance', methods=['GET', 'POST'])
def charge_balance():
    if request.method == 'POST':
        amount = request.form['amount']
        log_conn = sqlite3.connect("account_database.db")
        log_cur = log_conn.cursor()
        log_cur.execute("select * from login")
        log_cur.execute("UPDATE login SET money = '{}' WHERE email = '{}'"
                        .format(int(balance)+int(amount), email))
        log_conn.commit()
        log_conn.close()
        return redirect(url_for('information'))
    return render_template("charge_balance.html")


@app.route('/export')
def export():
    conn = sqlite3.connect('shopping_database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    conn.close()
    return render_template("shopping.html", rows=rows)


@app.route('/shopping', methods=['POST', 'GET'])
def shopping():
    global item, number
    error = None
    conn = sqlite3.connect('shopping_database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    if request.method == 'POST':
        email = request.form['email']
        product = request.form['product']
        quantity = request.form['quantity']
        if len(rows) != 0:
            for row in rows:
                if row[0] == product and int(row[1]) >= int(quantity) > 0 and email in rows:
                    shop_conn = sqlite3.connect("shopping_database.db")
                    shop_conn.row_factory = sqlite3.Row
                    shop_cur = shop_conn.cursor()
                    shop_cur.execute("select * from shopping")
                    shop_rows = shop_cur.fetchall()
                    for shop_row in shop_rows:
                        if str(shop_row[0]) == str(product):
                            number = shop_row[1]
                            item = shop_row[2]
                            break
                    count = number
                    price = item
                    log_conn = sqlite3.connect("account_database.db")
                    log_conn.row_factory = sqlite3.Row
                    log_cur = log_conn.cursor()
                    log_cur.execute("select * from login")
                    log_rows = log_cur.fetchall()
                    for log_row in log_rows:
                        if str(log_row[0]) == str(email):
                            if int(log_row[2])-(int(price) * int(quantity)) < 0:
                                break
                            log_cur.execute("UPDATE login SET money = '{}' WHERE email = '{}'"
                                            .format(int(log_row[2])-(int(price)*int(quantity)), email))
                            log_conn.commit()
                            log_conn.close()
                            if int(count) - int(quantity) == 0:
                                shop_conn.execute("DELETE FROM shopping")
                            else:
                                shop_cur.execute("UPDATE shopping SET num = '{}' WHERE email = '{}'"
                                                 .format(int(count)-int(quantity), email))
                            shop_conn.commit()
                            shop_conn.close()
                            return render_template("order.html")
                    error = " not enough money, charge the amount."
                    return render_template("purchase.html", rows=rows, error=error)
                else:
                    error = ' invalid product name or product quantity, try to enter again.'
                    conn.close()
        else:
            error = ' invalid product name or product quantity, try to enter again.'
            conn.close()
    return render_template("purchase.html", rows=rows, error=error)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        accept = True
        shop_item = request.form['item']
        shop_num = request.form['num']
        shop_price = request.form['price']
        if shop_item == '' or shop_num == '' or shop_price == '':
            return redirect(url_for('export'))
        with sqlite3.connect('shopping_database.db') as shop_conn:
            shop_conn.row_factory = sqlite3.Row
            shop_cur = shop_conn.cursor()
            shop_cur.execute("select * from shopping")
            shop_rows = shop_cur.fetchall()
            for shop_row in shop_rows:
                if shop_item == shop_row[0]:
                    accept = False
            if accept:
                shop_cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ?, ?)", (shop_item, shop_num, shop_price))
                shop_conn.commit()
            return redirect(url_for('export'))


@app.route('/celebrity_face_recognition', methods=['POST', 'GET'])
def celebrity_face_recognition():
    error = None
    response = None

    client_id = "private"
    client_secret = "private"

    url = "https://openapi.naver.com/v1/vision/celebrity"

    if request.method == 'POST':
        image = request.form['image']
        try:
            img = 'img/' + image
            files = {'image': open(img, 'rb')}
            headers = {'X-Naver-Client-ID': client_id, 'X-Naver-Client-Secret': client_secret}
            response = requests.post(url, files=files, headers=headers)
            rescode = response.status_code
        except FileNotFoundError:
            response = None
            if '.' in image:
                rescode = " file does not exist or has been deleted."
            else:
                rescode = " you did not enter an extension or you entered an incorrect extension."
            error = rescode
        except PermissionError:
            response = None
            rescode = ' email contains invalid special characters.'
            error = rescode

        if rescode == 200:
            print(response.text)
        else:
            print("Error Code:" + str(rescode))

    try:
        return render_template("celebrity_face_recognition.html", error=error, response=json.loads(response.text)["faces"][0]["celebrity"]["value"])
    except AttributeError:
        return render_template("celebrity_face_recognition.html", error=error, response=response)


if __name__ == '__main__':
    app.run()
