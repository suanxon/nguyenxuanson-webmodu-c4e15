from flask import *
from mongoengine import Document, StringField, IntField, BooleanField, ListField
from models.service import Service
from random import choice
import mlab
mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    services = Service.objects
    return render_template('index.html', all_services = services)

@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender = gender, height__gte =160, address__iexact = 'Hà Nội')

    return render_template('search.html', all_services = services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)

@app.route('/detail/<service_id>')
def detail(service_id):
    service_display = Service.objects.with_id(service_id)
    return render_template('detail.html', service_display = service_display)

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
        image = form['image']
        gender = form['gender']
        height = form['height']
        address = form['address']
        measure1 = form['measure1']
        measure2 = form['measure2']
        measure3 = form['measure3']
        measurements = [measure1, measure2, measure3]
        description = form['description']
        new_service = Service(image = image,
                              name = name,
                              yob = yob,
                              phone = phone,
                              gender = gender,
                              height = height,
                              address = address,
                              description = description,
                              measurements = measurements,
                              status = choice([True, False])
                              )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update_service/<service_id>', methods =['GET', 'POST'] )
def update_service(service_id):
    service_update = Service.objects.with_id(service_id)
    if request.method == 'GET':
        return render_template('update_service.html', services =service_update)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        service_update.update(set__name = name,
                              set__yob = yob,
                              set__gender = gender
                              )
        service_update.reload()
    return redirect(url_for('admin'))
@app.route('/delete_all')
def delete_all():
    service_delete = Service.objects()
    service_delete.delete()
    return "Done!"



if __name__ == '__main__':
  app.run(debug=True)
