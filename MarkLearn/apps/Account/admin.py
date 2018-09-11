# 全局配置
import xadmin
from .models import EmailVerifyRecord
from xadmin import views

"""
 使用Xadmin的主题功能。
 把全站的配置放在users\admin.py中:
 绑定之后,后台可以选择自己喜欢的主题
"""


# 创建xadmin的最基本管理器配置，并与view绑定


class BaseSetting(object):
    use_bootswatch = True


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = 'CareFree后台管理系统'
    # 修改footer
    site_footer = 'Copyright © 2018 CareFree Systems Incorporated. All rights reserved. 开发成员:陈志轩,廖智勇,王鹭星.张恺庭,黄凯'
    # 收起菜单
    menu_style = 'accordion'


# xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段
    search_fields = ['code']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)
