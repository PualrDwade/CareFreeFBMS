# Generated by Django 2.0.7 on 2018-09-17 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TraverAsk', '0002_auto_20180915_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='回答时间'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间'),
        ),
    ]