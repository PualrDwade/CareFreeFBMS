import xadmin
from .models import CityMsg
from .models import ScenicMsg
from .models import ProvinceMsg


# Register your models here.
class CityMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'province_name','img_url']
    # 搜索的字段
    search_fields = ['id', 'name']
    # 过滤
    list_filter = ['id', 'name', 'province_name','img_url']



class ScenicMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'city_name','img_url']
    # 搜索的字段
    search_fields = ['name','city_name','img_url']
    # 过滤
    list_filter = ['id', 'name','city_name','img_url']


class ProvinceMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name','img_url']
    # 搜索的字段
    search_fields = ['name','img_url']
    # 过滤
    list_filter = ['id', 'name', 'img_url']


# 使用xadmin进行数据字段的注册
xadmin.site.register(CityMsg, CityMsgAdmin)
xadmin.site.register(ScenicMsg, ScenicMsgAdmin)
xadmin.site.register(ProvinceMsg, ProvinceMsgAdmin)
