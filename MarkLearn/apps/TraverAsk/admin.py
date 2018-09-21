import xadmin
from .models import UserAsk
from .models import UserAnswer
from .models import TraverNote


# Register your models here.

class UserAskAdmin(object):
    # 显示的列
    list_display = ['id', 'title', 'ask_content', 'star_num', 'user_id',
                    'add_time', 'city_id']
    # 搜索的字段
    search_fields = ['title']
    # 过滤
    list_filter = ['id', 'title', 'user_id', 'add_time', 'city_id']


class UserAnswerAdmin(object):
    # 显示的列
    list_display = ['id', 'answer_content', 'ask_id', 'add_time','user_id']
    # 搜索的字段
    search_fields = ['id','answer_content']
    # 过滤
    list_filter = ['id', 'ask_id', 'add_time','user_id']


class TraverNoteAdmin(object):
    # 显示的列
    list_display = ['id', 'title', 'user_id', 'note_content',
                    'star_num', 'notify_status', 'add_time', 'img_url', 'city_id']
    # 搜索的字段
    search_fields = ['title',
                     'notify_status']
    # 过滤
    list_filter = ['id', 'title', 'user_id',
                   'notify_status', 'add_time', 'img_url', 'city_id']


# 使用xadmin进行注册
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserAnswer, UserAnswerAdmin)
xadmin.site.register(TraverNote, TraverNoteAdmin)
