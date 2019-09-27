# Generated by Django 2.1.5 on 2019-04-19 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Room', verbose_name='会议室'),
        ),
        migrations.AlterField(
            model_name='book',
            name='time_id',
            field=models.CharField(choices=[(1, '8:00'), (2, '9:00'), (3, '10:00'), (4, '11:00'), (5, '12:00'), (6, '13:00'), (7, '14:00'), (8, '15:00'), (9, '16:00'), (10, '17:00'), (11, '18:00'), (12, '19:00'), (13, '20:00'), (14, '21:00')], max_length=255, verbose_name='预定时段'),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='room',
            name='caption',
            field=models.CharField(max_length=36, verbose_name='会议室'),
        ),
        migrations.AlterField(
            model_name='room',
            name='max_num',
            field=models.IntegerField(verbose_name='最大人数'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='telephone',
            field=models.CharField(max_length=36, verbose_name='电话'),
        ),
    ]