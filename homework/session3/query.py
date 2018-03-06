import mlab
from models.service import Service

mlab.connect()
#
# all_services = Service.objects()
#
# first_service = all_services[100]
#

# print(first_service.address)


id_to_find = "5a955a3efd860d06203d7a3b"
# tim theo id
service = Service.objects().with_id(id_to_find)
print(service.to_mongo())

if service is not None:
    # service.delete()
    service.update(set__yob= 1998)
    service.reload()
    print(service.to_mongo())
else:
    print('Not found')
#xoa theo id
#sout.delete()
