from flask import Flask, render_template

app = Flask(__name__)

temp_list = []
string = ''

@app.route('/')
def default_setting():
    for i in range(1, 10):
        for j in range(1, 10):
            string = str(i)+' x '+str(j)+' = '+str(i*j)
            temp_list.append(string)
    return render_template('multiplication.html', len=len(temp_list), temp_list=temp_list)

if __name__ == '__main__':
    app.run()
