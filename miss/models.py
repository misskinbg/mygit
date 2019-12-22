from django.db import models

# Create your models here.
#coding:utf8

from django.db import models
from django.contrib.auth.models import User

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Student(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=30)
    age = models.IntegerField(verbose_name='年龄',default=18)
    xuehao = models.CharField(verbose_name='学号',max_length=11)
    mima = models.CharField(verbose_name='密码',max_length=15,default='201701811')



class Class(models.Model):
    gg = models.CharField(verbose_name='学号',max_length=12,default='201701811')
    aa = models.CharField(verbose_name='课程',max_length=30)
    bb = models.DecimalField(verbose_name='学分',max_digits=2,decimal_places=1,null=True,blank=True) # 最大位数和小数位多少
    cc = models.CharField(verbose_name='类别',max_length=30)
    dd = models.CharField(verbose_name='考核方式',max_length=30)
    ee = models.DecimalField(verbose_name='成绩',max_digits=4,decimal_places=1,null=True,blank=True)
    ff = models.DecimalField(verbose_name='绩点',max_digits=2,decimal_places=1,null=True,blank=True)

class teacher(models.Model):
    num = models.CharField(verbose_name='教师编号',max_length=6,default='000001')
    name = models.CharField(verbose_name='姓名',max_length=30)
    zhicheng = models.CharField(verbose_name='职称',max_length=30)

