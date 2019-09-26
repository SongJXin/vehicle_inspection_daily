import simplejson as simplejson
from django.contrib.auth.models import auth
from django.http import request
from django.contrib.auth.models import User
def login(request):
    body = simplejson.loads(request.body)
    username = body["username"]
    password = body["password"]

    user = auth.authenticate(username=username,password=password)
    if user:
        auth.login(request,user)
        return True
    else:
        return False