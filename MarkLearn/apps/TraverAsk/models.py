from datetime import datetime

from django.db import models

from Account.models import Signon
from TraverMsg.models import CityMsg

"""
总共三张表
UseAsk 用户问题
UserAnswer  用户回答
TraverNoteNote 用户游记
"""


# 1.UserAsk用户问题
class UserAsk(models.Model):
    # 设置问题id为主键
    id = models.CharField('问题id', primary_key=True, max_length=20)
    title = models.CharField('标题', max_length=100)
    ask_content = models.CharField('内容', max_length=3000)
    star_num = models.CharField('关注数', max_length=50)
    user_id = models.ForeignKey(Signon, verbose_name='所属用户', on_delete=models.CASCADE)
    add_time = models.DateTimeField('发表时间')
    # 以景点id为外键
    city_id = models.ForeignKey(CityMsg, verbose_name='所属城市id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户提问'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 2.UserAnswer用户解答
class UserAnswer(models.Model):
    # 设置主键
    id = models.CharField('回复id', primary_key=True, max_length=20)
    answer_content = models.CharField('回答内容', max_length=3000)  # 回答内容暂时给3000字数以内
    ask_id = models.ForeignKey(UserAsk, verbose_name='所属问题', on_delete=models.CASCADE)
    add_time = models.DateTimeField('回答时间')
    user_id = models.ForeignKey(Signon, verbose_name='所属用户', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户解答'
        verbose_name_plural = verbose_name



# 3.TraverNote用户游记
class TraverNote(models.Model):
    # 设置审核状态
    notify_choice = (
        ('1', '待评审'),
        ('2', '通过审核')
    )
    # 设置主键
    id = models.CharField('游记id', primary_key=True, max_length=200)
    title = models.CharField('标题', max_length=50)
    user_id = models.ForeignKey(Signon, verbose_name='所属用户', on_delete=models.CASCADE)
    note_content = models.CharField('游记内容', max_length=3000)  # 游记内容限定3000字以内
    star_num = models.CharField('点赞人数', max_length=10)
    notify_status = models.CharField('审核状态', max_length=10, choices=notify_choice, default='1')
    add_time = models.DateField('发表日期', default=datetime.now)
    img_url = models.CharField('封面图url', max_length=100)
    city_id = models.ForeignKey(CityMsg, verbose_name='所属城市', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户游记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
