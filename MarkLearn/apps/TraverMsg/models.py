# Create your models here.
# 行程信息模块的数据
from django.db import models
from Account.models import UserProfile

"""
# 1.省份信息
"""


class ProvinceMsg(models.Model):
    id = models.CharField('省份id',max_length=20, primary_key=True)
    name = models.CharField('省份名称', max_length=20)
    province_content = models.CharField('省份简介', max_length=500, null=True, blank=True)
    img_url = models.CharField('图片url', max_length=100, null=True, blank=True)

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
    name = models.CharField('城市名称', max_length=20)
    city_content = models.CharField('城市简介', max_length=500, null=True, blank=True)
    img_url = models.CharField('首页图片url', max_length=100, null=True, blank=True)
    province = models.ForeignKey(ProvinceMsg, verbose_name='所属省份', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 3.行程信息
"""


class TraverMsg(models.Model):
    # 创建旅游类型
    type_choices = (
        ('single', '自驾游'),
        ('together', '跟团游')
    )
    id = models.CharField('行程id', max_length=20, primary_key=True)
    name = models.CharField('行程名称', max_length=20)
    user_id = models.ForeignKey(UserProfile, verbose_name='所属用户', on_delete=models.CASCADE)
    start_city = models.ForeignKey(CityMsg, verbose_name='开始城市', on_delete=models.CASCADE, related_name='start_city_id')
    end_city = models.ForeignKey(CityMsg, verbose_name='目标城市', on_delete=models.CASCADE, related_name='end_city_id')
    traverdays = models.CharField('行程天数', max_length=3)
    adult_num = models.CharField('成人数量', max_length=3)
    child_num = models.CharField('儿童数量', max_length=3)
    traver_type = models.CharField('旅游类型', max_length=10, choices=type_choices, default='single')

    class Meta:
        verbose_name = '行程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name  # 返回基类的用户名


"""
# 4.景点信息
"""


class ScenicMsg(models.Model):
    id = models.CharField('景点id', max_length=20, primary_key=True)
    name = models.CharField('景点名称', max_length=20)
    city_id = models.ForeignKey(CityMsg, verbose_name='所属城市', on_delete=models.CASCADE)
    scenic_content = models.CharField('景点简介', max_length=500)
    img_url = models.CharField('首页图片url', max_length=100)  # url统一给100

    class Meta:
        verbose_name = "景点信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
