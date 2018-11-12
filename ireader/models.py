from django.db import models

# Create your models here.

#作者的实体类
from tinymce.models import HTMLField


class AuthorInfo(models.Model):
    sex_c=(('男','男'),('女','女'))
    #作者名
    nickname=models.CharField(max_length=255,verbose_name='作者')
    #作者简介
    jianjie=models.TextField(verbose_name="作者简介")
    #作者性别
    sex=models.CharField(choices=sex_c,max_length=255,verbose_name="性别")
    def __str__(self):
        return self.nickname
    class Meta:
        verbose_name_plural='作者管理'

#图书分类
class BookTypeInfo(models.Model):
    #书的类别
    typename=models.CharField(max_length=255,verbose_name='类别')
    #书的评价
    #remark=models.TextField(verbose_name="本书评价")
    def __str__(self):
        return self.typename
    class Meta:
        verbose_name_plural='图书分类'

#写作进度的表
class WorkProcess(models.Model):
    process=models.CharField(max_length=255,verbose_name='写作进度')
    def __str__(self):
        return self.process
    class Meta:
        verbose_name_plural='写作进度'

#属性
class BookProperty(models.Model):
    property=models.CharField(max_length=255,verbose_name="作品性质")
    def __str__(self):
        return self.property
    class Meta:
        verbose_name_plural='作品性质'

#幻灯片管理


#图书
class BookInfo(models.Model):
    #书名
    bname=models.CharField(max_length=255,verbose_name="书名")
    #作品封面
    bpic = models.ImageField(upload_to="poster/%Y/%m/%d", verbose_name="本书封面", blank=True, null=True)
    #是否推荐
    ishot = models.BooleanField(verbose_name="是否推荐")
    # 是否经典推荐
    ishot0 = models.BooleanField(verbose_name="是否经典推荐")
    #作品分类
    btype=models.ForeignKey(BookTypeInfo,on_delete=models.CASCADE,verbose_name="作品分类")
    #作品连载状态
    bprocess=models.ForeignKey(WorkProcess,on_delete=models.CASCADE,verbose_name="连载状态")
    #最后更新时间
    lastupdatime=models.DateField(verbose_name="最后更新时间")
    #作者
    author=models.ForeignKey(AuthorInfo,on_delete=models.CASCADE,verbose_name="作者")
    #评分
    score = models.FloatField(verbose_name="评分")
    #作品性质 免费等
    bproperty=models.ForeignKey(BookProperty,on_delete=models.CASCADE,verbose_name="作品性质")
    #全文字数
    words=models.IntegerField(verbose_name="全文字数")
    #章结数
    #chapers=models.CharField(max_length=255,verbose_name="总章节数")
    #收藏数
    #collect=models.IntegerField(verbose_name="收藏数")
    #总点击数
    allhit=models.IntegerField(verbose_name="点击数")
    #月点击数
    #monthhit=models.IntegerField(verbose_name="月点击数")
    #周点击数
    #weekhit=models.IntegerField(verbose_name="周点击数")
    #总推荐数
    allgroom=models.IntegerField(verbose_name="总推荐数")
    #月推荐数
    #monthgroom=models.IntegerField(verbose_name="月推荐数")
    #周推荐数
    weekgroom=models.IntegerField(verbose_name="周推荐数")
    #内容介绍
    context=models.TextField(verbose_name="内容简介")
    class Meta:
        verbose_name_plural='书籍添加'
class SlideInfo(models.Model):
    sname=models.CharField(max_length=255,verbose_name="幻灯片名称")
    spic=models.ImageField(upload_to="pic",verbose_name="大幻灯片的路径",blank=True,null=True)
    enabled=models.BooleanField(verbose_name="是否可用")
    slide_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="小说id")
    #内容介绍
    context=models.TextField(verbose_name="内容简介")
    class Meta:
        verbose_name_plural = "幻灯片管理"
class Chaper(models.Model):
    id=models.IntegerField()
    cname=models.CharField(primary_key=True,max_length=255,verbose_name="章节名")

    context = HTMLField("章节内容", null=True)

    resid=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name="章节")







