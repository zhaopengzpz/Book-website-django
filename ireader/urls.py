#coding=utf-8
from django.conf.urls import *
from . import views

urlpatterns = [
    #
    url("^$",views.index)
]