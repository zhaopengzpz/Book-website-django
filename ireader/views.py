#coding=utf-8


# Create your views here.

from django.http import *
from django.shortcuts import render
from .models import *

def index(request):

    slidelist=SlideInfo.objects.all().filter(enabled=True)[0:5]#大幻灯片
    booktype=BookTypeInfo.objects.all()#所有性质
    bookinfo=BookInfo.objects.all().filter(ishot=True)[0:11]#推荐图书
    books=BookInfo.objects.filter().order_by('?')[:14]#所有图书


    context={'slideList':slidelist,'bookType':booktype,'bookInfo':bookinfo,'Books':books[:7],'Books2':books[7:]}
    return render(request,"ireader/index.html",context)

#书籍详情页面显示
def detail(request,id):
    print(id)
    res=BookInfo.objects.get(id=id)#书id

    booktype = BookTypeInfo.objects.all()#类型id


    context={'resinfo':res,'bookType':booktype}

    return render(request, "ireader/book.html",context)
def showchapter(request,id):
    Cha = Chaper.objects.filter(resid=id)#类型id
    book=BookInfo.objects.get(id=id)
    context={'Chaper':Cha,'book':book}

    return render(request, "ireader/showchapter.html",context)
def pa(request):
    return render(request, "ireader/base.html")
#书籍列表页面  书库显示
def list(request):
    booktype = BookTypeInfo.objects.all()

    process=WorkProcess.objects.all()

    bp=BookProperty.objects.all()

    book=BookInfo.objects.all()[:12]

    context={'bookType':booktype,'pro':process,'bp':bp,'book':book}

    return render(request,"ireader/list.html",context)

#小说页面显示
def player(request,id,cid):
    content = Chaper.objects.get(id=cid,resid=id)  # id的章节
    book=BookInfo.objects.get(pk=id)
    count = Chaper.objects.filter(resid=id).count()
    #上一章，下一张判断
    if(int(cid) != 1):
        last = int(cid)-1
    else:
        last = int(cid)
    if(int(id) != count):
        next= int(cid)+1
    else:
        next = int(cid)
    context={'bk':book,"con":content,"co":next,"la":last}
    return render(request,"ireader/chapter.html",context)