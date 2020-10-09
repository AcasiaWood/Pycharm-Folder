from flask import Flask, render_template, request
import os
import shutil

app = Flask(__name__)

@app.route('/')
def default_setting():
    return render_template('image_input.html')

@app.route('/home', methods=['GET', 'POST'])
def image():
    path = 'static/'
    file_list = os.listdir(path)
    additional_path = os.listdir('./')
    if request.method == 'POST':
        file_name = request.form['image']
    file_name = file_name + '.png'
    image_check(additional_path, file_name, file_list)

def image_check(additional_path, file_name, file_list):
    if file_name in file_list:
        return render_template('image_static.html', file_name=file_name)
    else:
        for file in additional_path:
            try:
                if file_name in os.listdir(str(file) + '/'):
                    shutil.copy(file + '/' + file_name, 'static/')
                    return 'replaced with images from other folders.'
            except NotADirectoryError:
                pass

if __name__ == '__main__':
    app.run()
