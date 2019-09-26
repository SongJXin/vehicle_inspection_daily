from backend import models
from django.db.models import Count
from django.db.models import Sum
import simplejson as simplejson
from datetime import date
import datetime
def get_one_month_number():
    vehicle_type = models.Vehicle_Type.objects.values()
    type_list = [ type["type"] for type in vehicle_type  ]
    result = {}
    for type in type_list:
        result[type] = [0 for i in range(0,31)]
    today = date.today()
    oneMonth = datetime.timedelta(days=31)
    lastMonth = today - oneMonth
    vrobjects = models.Vehicles_Record.objects.filter(date__range=(lastMonth, today)).values("date","vehicle_type").annotate(count=Count("id"))
    for vrobject in vrobjects:
        diffDay =30 - (today - vrobject['date']).days
        result[vrobject['vehicle_type']][diffDay] = vrobject["count"]
    return str(result)
def get_one_month_totle_price():
    vehicle_type = models.Vehicle_Type.objects.values()
    type_list = [ type["type"] for type in vehicle_type  ]
    result = {}
    for type in type_list:
        result[type] = [0 for i in range(0,31)]
    today = date.today()
    oneMonth = datetime.timedelta(days=31)
    lastMonth = today - oneMonth
    vrobjects = models.Vehicles_Record.objects.filter(date__range=(lastMonth, today)).values("date","vehicle_type").annotate(totle=Sum('price'))
    for vrobject in vrobjects:
        diffDay = 30 - (today - vrobject['date']).days
        result[vrobject['vehicle_type']][diffDay] = vrobject["totle"]
    return str(result)
def get_pass(request):
    body = simplejson.loads(request.body)
    if body["classify"] == "week":
        day=7
    elif body["classify"] == "month":
        day=30
    else:
        day=1
    today = date.today()
    oneMonth = datetime.timedelta(days=day)
    lastMonth = today - oneMonth
    return models.Vehicles_Record.objects.values("status") \
        .filter(date__range=(lastMonth, today)) \
        .annotate(totle=Count('id'))