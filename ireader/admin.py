from django.contrib import admin
from . models import *
# Register your models here.

#为作者做个性化
class AuthorInfoAdmin(admin.ModelAdmin):
    #列表页面显示的内容
    list_display = ['nickname','sex']
    #分类汇总
    list_filter = ['nickname']
    #根据某个字段做搜索
    search_fields = ['nickname']
    #每页显示的数据
    list_per_page = 10
    #根据某个字段坐排序
    ordering = ['nickname']

admin.site.register(AuthorInfo,AuthorInfoAdmin)

class BookTypeInfoAdmin(admin.ModelAdmin):
    # 列表页面显示的内容
    list_display = ['typename']
    #每页显示的数据
    list_per_page = 10
admin.site.register(BookTypeInfo,BookTypeInfoAdmin)


class ChaperInline(admin.TabularInline):
    model = Chaper
    # 默认是三个


#图书
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['bname','author','btype']
    search_fields = ['bname']
    list_filter = ['btype']
    inlines = [ChaperInline]
admin.site.register(BookInfo,BookInfoAdmin)

#图书的性质
class BookPropertyAdmin(admin.ModelAdmin):
    list_display = ['property']
admin.site.register(BookProperty,BookPropertyAdmin)


#写作的进度
class WorkProcessAdmin(admin.ModelAdmin):
    list_display = ['process']

admin.site.register(WorkProcess,WorkProcessAdmin)

#幻灯片管理
class SlideInfoAdmin(admin.ModelAdmin):
    list_display = ['sname']
admin.site.register(SlideInfo,SlideInfoAdmin)

