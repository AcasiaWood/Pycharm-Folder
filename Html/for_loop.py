from flask import Flask, render_template

app = Flask(__name__)

color_list = ["Red", "Blue", "Yellow", "Green", "Purple", "Pink", "Gray", "Brown", "Black"]

@app.route('/')
def default_setting():
    return render_template('html/for_loop.html', len=len(color_list), color_list=color_list)

if __name__ == '__main__':
    app.run()
