import xadmin
from .models import CityMsg
from .models import TraverMsg
from .models import ScenicMsg
from .models import ProvinceMsg


# Register your models here.
class CityMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'city_content', 'img_url', 'province']
    # 搜索的字段
    search_fields = ['id', 'name']
    # 过滤
    list_filter = ['id', 'name', 'city_content', 'img_url', 'province']


class TraverMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'user_id', 'start_city', 'end_city',
                    'traverdays', 'adult_num', 'child_num', 'traver_type']
    # 搜索的字段
    search_fields = ['name', 'traver_type']
    # 过滤
    list_filter = ['id', 'name', 'user_id', 'start_city', 'end_city',
                   'traverdays', 'adult_num', 'child_num', 'traver_type']


class ScenicMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'city_id', 'scenic_content', 'img_url']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['id', 'name', 'city_id', 'img_url']


class ProvinceMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'province_content', 'img_url']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['id', 'name', 'img_url']


# 使用xadmin进行数据字段的注册
xadmin.site.register(CityMsg, CityMsgAdmin)
xadmin.site.register(TraverMsg, TraverMsgAdmin)
xadmin.site.register(ScenicMsg, ScenicMsgAdmin)
xadmin.site.register(ProvinceMsg, ProvinceMsgAdmin)
