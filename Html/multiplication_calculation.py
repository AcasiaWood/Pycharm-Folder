from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def default_setting():
    return render_template('multiplication_calculation.html')

@app.route('/home', methods=['GET', 'POST'])
def calculation():
    string_list = []
    if request.method == 'POST':
        number = request.form['number']
    for i in range(1, 10):
        string = "{} x {} = {}".format(int(number), int(i), int(number)*int(i))
        string_list.append(string)
    return render_template('multiplication_print.html', len=len(string_list), string_list=string_list)

if __name__ == '__main__':
    app.run()
