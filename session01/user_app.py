from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('user.html')
@app.route('/user/<user_name>')
def user(user_name):
    user ={
        'son':{
            'tuoi': '26',
            'sex': 'nam',
            'so thich': 'da bong'
                },
        'yen':{
            'tuoi': '24',
            'sex': 'nu',
            'so_thich': 'hat'
                }
    }
    info = ''
    for v in user:
        if user_name == v:
            info = v
        else:
            info = 'not'
    return info
if __name__ == '__main__':
  app.run(debug=True)
