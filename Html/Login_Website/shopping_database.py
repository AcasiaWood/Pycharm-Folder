import sqlite3
from flask import Flask
from flask import render_template, request

conn = sqlite3.connect("database.db")
print("opened database successfully")
conn.execute("CREATE TABLE IF NOT EXISTS SHOPPING (item TEXT, num TEXT, price TEXT)")
print("table created successfully")
conn.close()

app = Flask(__name__)

@app.route('/')
def default_setting():
    return "welcome to online shopping mall."

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