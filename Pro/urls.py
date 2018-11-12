"""Pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static
from ireader.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #转发 正则表达式
    #^开头 $结束
    #include("ireader.urls")包含很多路径
    url(r"^$",include("ireader.urls")),

    url(r"^(\d+)$",detail,name="detail"),

    url(r"^showchapter/(\d+)$",showchapter,name="showchapter"),
    url(r"^chaoter/(\d+)/(\d+)$",player,name="chapter"),
    url(r"^list/",pa,name='pa'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
