from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num>')
def default_function(num=None):
    return render_template('intro_2.html', num=num)

@app.route('/cal', methods=['POST'])
def home():
    temp = request.form['num']
    if request.method == 'POST':
        return redirect(url_for('default_function', num=temp))

if __name__ == '__main__':
    app.run()