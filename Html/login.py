# -*- coding : utf-8 -*-
from flask import Flask, render_template, request, redirect, session, url_for

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

if __name__ == '__main__':
    app.run()