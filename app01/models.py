from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import auth
# Create your models here.

class Userinfo(AbstractUser):
    telephone = models.CharField(max_length=36,verbose_name='电话')
    class meta:
        verbose_name = '会议室'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural=verbose_name


class Room(models.Model):
    caption = models.CharField(max_length=36,verbose_name='会议室')
    max_num = models.IntegerField(verbose_name='最大人数')
    def __str__(self):
        return self.caption
    class Meta:
        verbose_name = '会议室'
        verbose_name_plural=verbose_name

class Book(models.Model):
    user = models.ForeignKey(to='Userinfo',on_delete=models.CASCADE,verbose_name='用户')
    room = models.ForeignKey(to='Room',on_delete=models.CASCADE,verbose_name='会议室')
    date = models.CharField(verbose_name='日期',max_length=36)
    time_choices = (
        (1,'8:00'),
        (2,'9:00'),
        (3,'10:00'),
        (4,'11:00'),
        (5,'12:00'),
        (6,'13:00'),
        (7,'14:00'),
        (8,'15:00'),
        (9,'16:00'),
        (10,'17:00'),
        (11,'18:00'),
        (12,'19:00'),
        (13,'20:00'),
        (14,'21:00'),
    )
    time_id = models.CharField(choices=time_choices,max_length=255,verbose_name='预定时段')

    class Meta:
        unique_together=(
            ('room','date','time_id')
        )
        verbose_name = '流程'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{}预定了{}'.format(self.user,self.room)