import mlab
from models.service import WarmWinter
from random import randint, choice

from faker import Faker
mlab.connect()

fake = Faker()

for i in range(50):
    print("Saving service ", i+1, "...")
    x = fake.profile()
    service = WarmWinter(name = fake.name(),
                      email = x['mail'],
                      gender = randint(0, 1),
                      company = x['company'],
                      job = x['job'],
                      phone = fake.phone_number(),
                      address = fake.address(),
                      contacted = choice([True, False])
                      )

    service.save()
