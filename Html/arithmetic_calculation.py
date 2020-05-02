from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def default_function():
    return render_template('arithmetic_calculation.html')

@app.route('/home', methods=['GET', 'POST'])
def calculation():
    if request.method == 'POST':
        first = request.form['first']
        operator = request.form['operator']
        second = request.form['second']
        if operator == '+':
            string = str(first) + ' + ' + str(second) + ' = ' + str(int(first)+int(second))
        elif operator == '-':
            string = str(first) + ' - ' + str(second) + ' = ' + str(int(first)-int(second))
        elif operator == '*':
            string = str(first) + ' * ' + str(second) + ' = ' + str(int(first)*int(second))
        elif operator == '/':
            string = str(first) + ' / ' + str(second) + ' = ' + str(int(first)/int(second))
        else:
            string = 'error occurred'
        return string

if __name__ == '__main__':
    app.run()