from backend import models
import simplejson as simplejson
def create(request):
    body = simplejson.loads(request.body)
    return models.Vehicle_Type.objects.create(
        type=body['type'],
        price=body['prices']
    )
def update():
    pass
def select_all():
    return models.Vehicle_Type.objects.values()
def delete(request):
    body = simplejson.loads(request.body)
    return  models.Vehicle_Type.objects.filter(
        type=body['type'],
        price=body['prices']
    ).delete()
def select_one(vType):
    return models.Vehicle_Type.objects.values(type=vType)