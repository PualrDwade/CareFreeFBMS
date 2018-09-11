from django.db import models
from TraverMsg.models import CityMsg
from TraverMsg.models import ScenicMsg
from TraverMsg.models import CityMsg

# Create your models here.
# 产品推荐展示模块


"""
# 1.供应商
"""


class Supplier(models.Model):
    # 创建合作等级类型
    type_choices = (
        ('1', '战略合作'),
        ('2', '广告代理'),
        ('3', '数据提供')
    )
    id = models.CharField('供应商id', max_length=20, primary_key=True)
    name = models.CharField('供应商名称', max_length=30)
    link_url = models.CharField('供应商网站链接', max_length=100)
    cooperation_type = models.CharField('合作类型', max_length=10, choices=type_choices, default='3')

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 2.产品信息
数据库当中用于选择的属性：起价、行程天数、出发城市、产品类型、景点、供应商、销量
"""


class ProductMsg(models.Model):
    traver_type = (
        ('1', '自驾游'),
        ('2', '跟团游')
    )

    id = models.CharField('产品id', max_length=20, primary_key=True)
    name = models.CharField('产品名称', max_length=30)
    traver_days = models.CharField('行程天数', max_length=10)
    start_city = models.ForeignKey(CityMsg, verbose_name='出发城市', on_delete=models.CASCADE)
    product_price = models.CharField('起价', max_length=10)
    product_type = models.CharField('产品类型', max_length=10, choices=traver_type, default='1')
    scenic_id = models.ForeignKey(ScenicMsg, verbose_name='景点id', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE)
    product_link = models.CharField('产品链接', max_length=100)
    score = models.CharField('综合评分', max_length=10)
    sell_num = models.CharField('产品销量', max_length=10)

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 3.门票信息
"""


class TicketsMsg(models.Model):
    id = models.CharField('门票id', max_length=20, primary_key=True)
    scenic_id = models.ForeignKey(ScenicMsg, verbose_name='所属景点', on_delete=models.CASCADE, null=True)
    name = models.CharField('门票名称', max_length=20)
    ticket_content = models.CharField('费用说明', max_length=3000, null=True)
    scense_address = models.CharField('场景地址', max_length=100, null=True)
    ticket_price = models.CharField('门票价格', max_length=10, null=True)
    ticket_link = models.CharField('门票链接', max_length=100)
    supplier_id = models.ForeignKey(Supplier, verbose_name='所属供应商', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '门票信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 4.酒店信息
"""


class HotelMsg(models.Model):
    type_choice = (
        ('1', '高档酒店'),
        ('2', '团购'),
        ('3', '特价酒店'),
        ('4', '客栈青旅')
    )
    id = models.CharField('酒店id', max_length=20, primary_key=True)
    name = models.CharField('酒店名字', max_length=50)
    type = models.CharField('酒店类型', choices=type_choice, default='4', max_length=20)
    score = models.CharField('酒店评分', max_length=10)
    hotel_price = models.CharField('酒店价格', max_length=10)
    hotel_content = models.CharField('酒店简介', max_length=300)
    city_id = models.ForeignKey(CityMsg, verbose_name='所属城市', on_delete=models.CASCADE)
    scenic_id = models.ForeignKey(ScenicMsg, verbose_name='所属景点', on_delete=models.CASCADE)
    img_url = models.CharField('图片url', max_length=100)
    supplier_id = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE)
    hotel_link = models.CharField('酒店链接', max_length=100)

    class Meta:
        verbose_name = '酒店信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 5.攻略信息
"""


class StrategyMsg(models.Model):
    id = models.CharField('攻略id', max_length=20, primary_key=True)
    title = models.CharField('标题', max_length=100)
    link_url = models.CharField('攻略链接', max_length=100)
    simple_content = models.CharField('简介', max_length=1000)
    supplier_id = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE)
    img_url = models.CharField('图片链接', max_length=100)
    city_id = models.ForeignKey(CityMsg, verbose_name='相关城市', on_delete=models.CASCADE, null=True)  # 允许为空
    scenic_id = models.ForeignKey(ScenicMsg, verbose_name='相关景点', on_delete=models.CASCADE, null=True)  # 允许为空

    class Meta:
        verbose_name = '攻略信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
