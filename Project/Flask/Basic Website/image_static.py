from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def default_setting():
    path = 'static/'
    file_list = os.listdir(path)
    file_name = file_list[random.randint(0, len(file_list)-2)]
    print("file_list: {}".format(file_list))
    return render_template('image_static.html', file_name=file_name)

if __name__ == '__main__':
    app.run()