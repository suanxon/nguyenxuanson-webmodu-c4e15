from mongoengine import Document, StringField, IntField, BooleanField

class WarmWinter(Document):   #Service là collections
    name = StringField()
    email = StringField()
    gender = IntField()
    company = StringField()
    job = StringField()
    phone = StringField()
    address = StringField()
    contacted = BooleanField()
