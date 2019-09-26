from django.shortcuts import render
from django.http import HttpResponseRedirect
from backend.src import auth
from django.http import HttpResponse
from backend.src import vehicle_type
from backend.src import vehicle_recoder
from backend.src import chart_data
from backend.src import tools
from backend import models
import simplejson as simplejson
# Create your views here.
from django.contrib.auth import authenticate,login
# 登陆  （暂时未启用）
def login(request):
    if request.method == 'POST':
        if auth.login(request):
            return HttpResponse("/")
        else:
            return HttpResponse("用户名/密码错误",status="403")
#删除 车辆类型
def delete_vehicle_type(request):
    return HttpResponse(vehicle_type.delete(request))
#新增车辆类型
def add_vehicle_type(request):
    return HttpResponse(vehicle_type.create(request))
# 获取所有车辆类型
def get_all_vehicle_type(request):
    #把list中的dict转化为str，然后把list转化为str，最后把单引号换成双引号（json要求kv都为双引号）
    vtstring = ",".join([str(vt) for vt in vehicle_type.select_all()]).replace("'",'"')
    return HttpResponse('{"result":['+vtstring+"]}")
#新增审车记录
def add_vehicle_recorder(request):
    return HttpResponse(vehicle_recoder.create(request))
#获取所有审车记录
def get_all_vehicle_recorder(request):
    recoders,count = vehicle_recoder.select_all()
    vrstring = ",".join([str(vr) for vr in recoders]).replace("'",'"')
    return HttpResponse('{"result":['+vrstring+'],"count":'+str(count)+'}')
def get_vehicle_recorder(request):
    if request.method == 'POST':
        recoders,count = vehicle_recoder.select(request)
        vrstring = ",".join([str(vr) for vr in recoders]).replace("'", '"')
        return HttpResponse('{"result":['+vrstring+'],"count":'+str(count)+'}')
    else:
        return get_all_vehicle_recorder(request)
def delete_vehicle_recorder(request):
    return HttpResponse(vehicle_recoder.delete(request))
def recoder_number_by_type(request):
    return HttpResponse(chart_data.get_one_month_number().replace("'",'"'))
def recoder_totle_by_type(request):
    return HttpResponse(chart_data.get_one_month_totle_price().replace("'",'"'))
def pass_or_not(request):
    return HttpResponse(chart_data.get_pass(request))
def collect_get(request):
    collection,totle,datestr = vehicle_recoder.collect(request)
    collectionstr = ",".join([str(cl) for cl in collection]).replace("'",'"')
    return HttpResponse('{"result":['+collectionstr+'],"totle":"'+ tools.digital_to_chinese(totle["totle"])+'('+str(totle["totle"])+')","datestr":"'+ datestr +'"}')