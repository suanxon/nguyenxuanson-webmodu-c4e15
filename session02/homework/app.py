from flask import Flask, render_template
from mongoengine import Document, StringField, IntField, BooleanField
from models.service import WarmWinter
import mlab
mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    services = WarmWinter.objects(gender = gender, contacted = False)
    ten_services = services[0:10]

    return render_template('search.html', all_services = ten_services)


if __name__ == '__main__':
  app.run(debug=True)
