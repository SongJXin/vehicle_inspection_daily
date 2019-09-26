"""car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from backend import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('login',views.login),
    path('settings/vehicle_type/get_all',views.get_all_vehicle_type),
    path('settings/vehicle_type/create',views.add_vehicle_type),
    path('settings/vehicle_type/delete',views.delete_vehicle_type),
    path('recorder/add',views.add_vehicle_recorder),
    path('recorder/get/all',views.get_all_vehicle_recorder),
    path('recorder/search',views.get_vehicle_recorder),
    path('recorder/delete',views.delete_vehicle_recorder),
    path('charts/recorder/number',views.recoder_number_by_type),
    path('charts/recorder/totle',views.recoder_totle_by_type),
    path('charts/recorder/pass',views.pass_or_not),
    path('collect/get',views.collect_get)
]
