from flask import *
from mongoengine import Document, StringField, IntField, BooleanField
from models.service import Service
import mlab
mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender = gender, height__gte =160, address__iexact = 'Hà Nội')

    return render_template('search.html', all_services = services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)
@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)
    if service_to_delete is None:
        return "Not found"

    service_to_delete.delete()
    return redirect(url_for('admin'))

@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form

        name = form['name']
        yob = form['yob']
        phone = form['phone']
        new_service = Service(name = name,
                              yob = yob,
                              phone = phone,
                              gender = 1,
                              height = 170,
                              address = 'HD',
                              status = True
                              )
        new_service.save()
        return "Saved"

@app.route('/delete_all')
def delete_all():
    service_delete = Service.objects()
    service_delete.delete()
    return "Done!"
    
if __name__ == '__main__':
  app.run(debug=True)
