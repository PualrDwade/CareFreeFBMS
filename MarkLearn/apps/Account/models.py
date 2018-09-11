# Create your models here.
# 用户模块的数据
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

"""
# 1.自定义userProfile
"""


class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField(
        '性别', max_length=10, choices=gender_choices, default='female')
    address = models.CharField('地址', max_length=100, default='')
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.CharField('头像', max_length=100)
    email = models.CharField('邮箱', max_length=30, default='')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username  # 返回基类的用户名


"""
# 2.EmailVerifyRecord验证码
"""


class EmailVerifyRecord(models.Model):
    # 使用元组的形式进行orm操作
    send_choices = (
        ('register', '注册'),
        ('forget', '找回密码')
    )

    code = models.CharField('验证码', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField('发送类型', choices=send_choices, max_length=10)
    send_time = models.DateTimeField('发送时间', default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
