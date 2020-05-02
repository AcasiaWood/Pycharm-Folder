from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def default_function():
    return render_template('intro_1.html')

@app.route('/home', methods=['POST'])
def cal():
    temp = request.form['hello']
    if temp == "hello":
        return "bye"
    else:
        return 'nice to meet you'

if __name__ == '__main__':
    app.run()