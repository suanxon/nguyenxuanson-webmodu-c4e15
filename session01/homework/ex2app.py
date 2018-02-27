from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<user_name>')
def user(user_name):
    article_title = 'Profile C4E15'
    name = user_name
    user_info ={
        'son': {
                'name': 'son',
                'age': '26',
                'sex':'male'
                },
        'yen':{
                'name': 'yen',
                'age': '22',
                'sex':'fumale'
                },
    }
    info = ''
    if name in user_info:
        info = user_info[name]
        return render_template('user_profile.html', article_title = article_title, info = info)
    else:
        return "Not found"

if __name__ == '__main__':
  app.run(debug=True)
