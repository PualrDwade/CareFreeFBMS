import xadmin
from .models import ProductMsg
from .models import Supplier
from .models import TicketsMsg
from .models import HotelMsg
from .models import StrategyMsg


# Register your models here.
# xadmin中这里是继承object，不再是继承admin
class ProductMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'traver_days', 'start_city',
                    'product_type', 'scenic_id', 'product_price', 'supplier',
                    'product_link', 'score', 'sell_num']
    # 搜索的字段
    search_fields = ['name', 'product_type']
    # 过滤
    list_filter = ['id', 'name', 'product_price', 'supplier',
                   'product_link', 'score', 'sell_num']


class SupplierAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'link_url', 'cooperation_type']
    # 搜索的字段
    search_fields = ['name', 'cooperation_type']
    # 过滤
    list_filter = ['id', 'name', 'link_url', 'cooperation_type']


class TicketMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'scenic_id', 'name', 'ticket_content', 'scense_address', 'ticket_price']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['id', 'scenic_id', 'name', 'ticket_content', 'ticket_price']


class HotelMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'type', 'score', 'hotel_price',
                    'hotel_content', 'scenic_id', 'img_url', 'supplier_id', 'hotel_link']
    # 搜索的字段
    search_fields = ['name', 'type']
    # 过滤
    list_filter = ['id', 'name', 'type', 'score', 'hotel_price',
                   'scenic_id', 'img_url', 'supplier_id', 'hotel_link']


class StrategyMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'title', 'link_url', 'simple_content', 'supplier_id', 'img_url', 'city_id', 'scenic_id']
    # 搜索的字段
    search_fields = ['title','link_url']
    # 过滤
    list_filter = ['id', 'title', 'link_url', 'simple_content', 'supplier_id', 'img_url', 'city_id', 'scenic_id']


# 将基本配置管理与view绑定
xadmin.site.register(Supplier, SupplierAdmin)
xadmin.site.register(ProductMsg, ProductMsgAdmin)
xadmin.site.register(TicketsMsg, TicketMsgAdmin)
xadmin.site.register(HotelMsg, HotelMsgAdmin)
xadmin.site.register(StrategyMsg, StrategyMsgAdmin)
