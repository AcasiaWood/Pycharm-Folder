from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

app.secret_key = b'1234abc'

conn = sqlite3.connect("join_info.db")
cur = conn.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS account(id TEXT, pwd TEXT)")
conn.commit()
conn.close()

@app.route('/')
def default_setting():
    return 'hello'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if not session.get('logged_in'):
        if request.method == 'POST':
            conn = sqlite3.connect("join_info.db")
            cur = conn.cursor()
            login_id = request.form.get('id', "not data")
            login_pwd = request.form.get('pwd', "not data")

            if login_id == "not data":
                return render_template('login.html')

            execute = "SELECT * FROM account where id = (?)"
            cur.execute(execute, login_id)
            rows = cur.fetchall()
            conn.commit()
            conn.close()

            try:
                if rows[0][1] == login_pwd:
                    print("login successfully")
                    session['logged_in'] = True
                    return redirect(url_for('welcome'))
            except:
                print("login unsuccessfully")
                return render_template('login.html')
    else:
        return redirect(url_for('welcome'))

    return render_template('login.html', error=error)

@app.route("/sign_up/", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        conn = sqlite3.connect("join_info.db")
        cur = conn.cursor()

        want_id = request.form.get('want_id', "not_data")
        want_pwd = request.form.get('want_pwd', "not_data")

        if want_id == "not_data":
            return render_template('join.html')
        execute = "INSERT INTO account(ID, PWD) VALUES(?, ?)"
        cur.execute(execute, (want_id, want_pwd))
        print("join successfully")
        try:
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except:
            print('join unsuccessfully')
            return render_template('join.html')

    else:
        return render_template("join.html")

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('/welcome'))

if __name__ == '__main__':
    app.run()
