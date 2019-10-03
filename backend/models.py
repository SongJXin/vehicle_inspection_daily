from django.db import models

# Create your models here.
# 汽车行驶证信息 （暂未启用）
class Vehicles_Detail(models.Model):
    plate_No        = models.CharField(primary_key=True,max_length=20)
    vehicle_type    = models.IntegerField()
    owner           = models.CharField(max_length=10)
    use_character   = models.CharField(max_length=10)
    VIN             = models.CharField(max_length=20)
    engine_No       = models.CharField(max_length=20)
    comment         = models.CharField(max_length=254)
# 审车记录
class Vehicles_Record(models.Model):
    id              = models.IntegerField(primary_key=True)
    date            = models.DateField()
    vehicle_type    = models.CharField(max_length=50)
    plate_no        = models.CharField(max_length=254)
    price           = models.FloatField()
    number          = models.IntegerField(default=1)
    totle           = models.FloatField(default=0)
    status          = models.CharField(max_length=20,blank=True)
    comment         = models.CharField(max_length=254,blank=True)
    recorder        = models.CharField(max_length=20,blank=True)

#审车缴费类型
class Vehicle_Type (models.Model):
    id              = models.IntegerField(primary_key=True)
    type            = models.CharField(max_length=254)
    price           = models.FloatField()
    comment         = models.CharField(max_length=254,blank=True)

#审车状态  通过/未通过 （暂未启用）
class Record_Status(models.Model):
    id              = models.IntegerField(primary_key=True)
    status          = models.CharField(max_length=254)
    comment         = models.CharField(max_length=254,blank=True)