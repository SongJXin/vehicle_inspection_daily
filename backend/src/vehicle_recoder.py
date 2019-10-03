from backend import models
import simplejson as simplejson
from datetime import date
import datetime
from django.db.models import Count
from django.db.models import Sum
import time
def create(request):
    body = simplejson.loads(request.body)
    price = body["price"]
    number = int(body["number"])
    return models.Vehicles_Record.objects.create(
        plate_no=body["plate_no"],
        vehicle_type=body["vehicle_type"],
        price=price,
        number=number,
        totle=price * number,
        status=body["status"],
        date=body["date"],
        comment=body["comment"],
        recorder=body["recorder"]
    )
def update(request):
    pass
def delete(request):
    body = simplejson.loads(request.body)
    return models.Vehicles_Record.objects.filter(id=body['id']).delete()
def select(request):
    body = simplejson.loads(request.body)
    if body['todate'] == "":
        todate = date.today()
    else:
        todate = datetime.datetime.strptime(body['todate'], "%Y-%m-%d")
    if body['fromdate'] == "":
        fromdate = date.today()
    else:
        fromdate = datetime.datetime.strptime(body['fromdate'],"%Y-%m-%d")
    status = body['status']
    vehicle_type = body['vehicle_type']
    plate_no = body["plate_no"]
    recodersObject = models.Vehicles_Record.objects.filter(date__range=(fromdate,todate))
    if status != "":
        recodersObject = recodersObject.filter(status=status)
    if vehicle_type != "":
        recodersObject = recodersObject.filter(vehicle_type=vehicle_type)
    if plate_no != "":
        recodersObject = recodersObject.filter(plate_no__contains=plate_no)
    recoders = recodersObject.values()
    count = recodersObject.count()
    for i in range(0,len(recoders)):
        recoders[i]['date'] = recoders[i]['date'].strftime('%Y-%m-%d')
    return recoders,count
def select_all():
    today = date.today()
    oneMonth = datetime.timedelta(days=0)
    lastMonth = today - oneMonth
    recodersObject = models.Vehicles_Record.objects.filter(date__range=(lastMonth,today))
    counts = recodersObject.count()
    recoders = models.Vehicles_Record.objects.filter(date__range=(lastMonth,today)).values()
    for i in range(0,len(recoders)):
        recoders[i]['date'] = recoders[i]['date'].strftime('%Y-%m-%d')
    return recoders,counts
def collect(request):
    body = simplejson.loads(request.body)
    if body['todate'] == "":
        todate = date.today()
    else:
        todate = datetime.datetime.strptime(body['todate'], "%Y-%m-%d")
    if body['fromdate'] == "":
        fromdate = date.today()
    else:
        fromdate = datetime.datetime.strptime(body['fromdate'],"%Y-%m-%d")
    if todate == fromdate:
        datestr = fromdate.strftime('%Yyear%mmonth%dday')
    else:
        datestr = fromdate.strftime('%Yyear%mmonth%dday')+ "-" + todate.strftime('%Yyear%mmonth%dday')
    datestr = datestr.replace("year","年").replace("month","月").replace("day","日")
    recodersObject = models.Vehicles_Record.objects.\
        filter(date__range=(fromdate, todate)).\
        values("vehicle_type","price").annotate(count=Sum("number"),totle=Sum("totle"))
    totle = models.Vehicles_Record.objects.filter(date__range=(fromdate, todate)).all().aggregate(totle=Sum("totle"))
    return recodersObject,totle,datestr