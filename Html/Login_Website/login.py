import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for

conn = sqlite3.connect("database.db")
print("opened database successfully")
conn.execute("CREATE TABLE IF NOT EXISTS SHOPPING (item TEXT, num TEXT, price TEXT)")
print("table created successfully")
conn.close()

app = Flask(__name__)

app.secret_key = 'admin'

@app.route('/')
def default_setting():
    return render_template('localhost.html')

def check_out(email, password):
    flag = False
    account = {'admin': '123456', 'user1': '654321', 'user2': '321654'}
    try:
        if account[email] == password:
            flag = True
    except IndexError:
        flag = False
    return flag

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if not session.get('logged_in'):
        if request.method == "POST":
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
    return redirect(url_for('login'))

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/shopping')
def shopping():
    # get a data from the database.
    conn_ = sqlite3.connect('database.db')
    conn_.row_factory = sqlite3.Row
    cur = conn_.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    print("DB: ")
    print(rows)
    return render_template("shopping.html", rows=rows)

@app.route('/database_add', methods=['POST', 'GET'])
def database_add():
    msg = ""
    if request.method == 'POST':
        try:
            item = request.form['item']
            num = request.form['num']
            price = request.form['price']
            with sqlite3.connect('database.db') as conn_:
                cur = conn_.cursor()
                cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ?, ?)", (item, num, price))
                conn_.commit()
                msg = "record successfully add"
                return render_template("shopping_add_result.html", message=msg)
        except:
            conn_.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("shopping_add.html", message=msg)

if __name__ == '__main__':
    app.run()