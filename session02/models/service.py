from mongoengine import Document, StringField, IntField, BooleanField, ListField

class Service(Document):   #Service là collections
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1:male
    height = IntField()
    image = StringField()
    phone = StringField()
    address = StringField()
    description = StringField()
    measurements = ListField()
    status = BooleanField()
