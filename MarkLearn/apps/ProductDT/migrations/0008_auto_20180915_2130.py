# Generated by Django 2.0.7 on 2018-09-15 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0007_auto_20180914_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelmsg',
            name='hotel_link',
            field=models.CharField(max_length=1000, verbose_name='酒店链接'),
        ),
        migrations.AlterField(
            model_name='hotelmsg',
            name='img_url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='图片url'),
        ),
        migrations.AlterField(
            model_name='productmsg',
            name='img_url',
            field=models.CharField(max_length=1000, verbose_name='图片url'),
        ),
        migrations.AlterField(
            model_name='productmsg',
            name='product_link',
            field=models.CharField(max_length=1000, verbose_name='产品链接'),
        ),
        migrations.AlterField(
            model_name='strategymsg',
            name='img_url',
            field=models.CharField(max_length=1000, verbose_name='图片链接'),
        ),
        migrations.AlterField(
            model_name='strategymsg',
            name='link_url',
            field=models.CharField(max_length=1000, verbose_name='攻略链接'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='img_url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='scense_address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='场景地址'),
        ),
        migrations.AlterField(
            model_name='ticketsmsg',
            name='ticket_link',
            field=models.CharField(max_length=1000, verbose_name='门票链接'),
        ),
    ]