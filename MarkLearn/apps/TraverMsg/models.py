# Create your models here.
# 行程信息模块的数据
from django.db import models


"""
# 1.省份信息
"""


class ProvinceMsg(models.Model):
    id = models.CharField('省份id',max_length=20, primary_key=True)
    name = models.CharField('省份名称', max_length=20,unique=True)
    img_url = models.CharField('图片url',max_length=100,null = True,blank=True)

    class Meta:
        verbose_name = '省份信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



"""
# 2.城市信息
"""


class CityMsg(models.Model):
    id = models.CharField('城市id', max_length=20, primary_key=True)
    name = models.CharField('城市名称', max_length=20,unique=True)
    img_url = models.CharField('首页图片url', max_length=100, null=True, blank=True)
    province_name = models.CharField('所属省份',max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

"""
# 3.景点信息
"""


class ScenicMsg(models.Model):
    id = models.CharField('景点id', max_length=20, primary_key=True)
    name = models.CharField('景点名称', max_length=20)
    img_url = models.CharField('图片url',max_length=100,null=True,blank=True)
    city_name = models.CharField('所属城市',max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = "景点信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
