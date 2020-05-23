import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for

conn = sqlite3.connect("shopping_database.db")
print("opened database successfully")
conn.execute("CREATE TABLE IF NOT EXISTS SHOPPING (item TEXT, num TEXT, price TEXT)")
print("table created successfully")

log_conn = sqlite3.connect("account_database.db")
print("opened database successfully")
log_conn.execute("CREATE TABLE IF NOT EXISTS LOGIN (email TEXT, password TEXT)")
print("table created successfully")

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

log_conn.row_factory = sqlite3.Row
cur = log_conn.cursor()
cur.execute("select * from login")
rows = cur.fetchall()

select = str(input('whether to delete account database (y/n): '))

if select == 'y':
    if len(rows) != 0:
        log_conn.execute("DELETE FROM login")
        log_conn.commit()
        print("table deleted successfully")
    else:
        print("error: there are no entries in table.")
else:
    print("table deleted unsuccessfully")

log_conn.close()

with sqlite3.connect('account_database.db') as log_conn:
    cur = log_conn.cursor()
    cur.execute("INSERT INTO login (email, password) VALUES (?, ?)", ('admin', '123456'))
    cur.execute("INSERT INTO login (email, password) VALUES (?, ?)", ('user1', '654321'))
    cur.execute("INSERT INTO login (email, password) VALUES (?, ?)", ('user2', '123654'))
    log_conn.commit()
    msg = "record successfully add"

app = Flask(__name__)

app.secret_key = 'admin'

@app.route('/')
def default_setting():
    return render_template('localhost.html')

def account_info():
    # get a data from the database.
    account = {}
    conn_ = sqlite3.connect('account_database.db')
    conn_.row_factory = sqlite3.Row
    cur = conn_.cursor()
    cur.execute("select * from login")
    rows = cur.fetchall()
    for number in range(len(rows)):
        account[rows[number][0]] = rows[number][1]
    return account, render_template("account.html", rows=rows)

def check_out(email, password):
    flag = False
    account, _ = account_info()
    print(account)
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
            email, password = request.form['email'], request.form['password']
            conn = sqlite3.connect('account_database.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from login")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == email:
                    flag = False
                    break
            if not flag:
                error = ' email already exists, try to register again.'
            else:
                session['logged_in'] = True
                cur.execute("INSERT INTO login (email, password) VALUES (?, ?)", (email, password))
                conn.commit()
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

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/export')
def export():
    # get a data from the database.
    conn = sqlite3.connect('shopping_database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    return render_template("shopping.html", rows=rows)

@app.route('/shopping', methods=['POST', 'GET'])
def shopping():
    error = None
    conn = sqlite3.connect('shopping_database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    if request.method == 'POST':
        product = request.form['product']
        quantity = request.form['quantity']
        if len(rows) != 0:
            for row in rows:
                if row[0] == product and row[1] >= quantity:
                    # TODO
                    # code to delete for each item, num, and price data is required.
                    return render_template("order.html")
                else:
                    error = ' invalid product name or product quantity, try to enter again.'
        else:
            error = ' invalid product name or product quantity, try to enter again.'
    return render_template("purchase.html", rows=rows, error=error)

@app.route('/database_add', methods=['POST', 'GET'])
def database_add():
    msg = ""
    if request.method == 'POST':
        try:
            item = request.form['item']
            num = request.form['num']
            price = request.form['price']
            with sqlite3.connect('shopping_database.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ?, ?)", (item, num, price))
                conn.commit()
                msg = "record successfully add"
                return render_template("shopping_add_result.html", message=msg)
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("shopping_add.html", message=msg)

if __name__ == '__main__':
    app.run()
