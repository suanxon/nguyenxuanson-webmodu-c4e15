import mlab
from models.service import Service

mlab.connect()

all_services = Service.objects()

first_service = all_services[100]

print(first_service.address)
