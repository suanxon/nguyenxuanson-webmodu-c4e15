from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello C4E15"

@app.route('/hello2/<name>')
def hello2(name):
    return "Hello " + name

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    return str(num1 + num2)

@app.route('/html')
def heading():
    return "<h1> ok con de </h1>"

@app.route('/blog')
def blog():
    article_name = "Thơ con cóc"
    posts = [
        {
            'content': 'Hôm nay tôi buồn',
            'author': "1"
        },
        {
            'content': 'Không biết vì sao tôi buồn',
            'author': '2'
        }
    ]

    return render_template('blog.html', article_title = article_name, posts = posts)


if __name__ == '__main__':
  app.run(debug=True)
