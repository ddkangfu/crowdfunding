#coding=utf-8
#!/usr/bin/python

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200) #项目名称
    description = models.TextField() #项目介绍
    limit_mondy = models.CharField(max_length=200) #众筹金额
    limit_date = models.DateTimeField() #众筹期限
    owner = models.ForeignKey(User) #项目发起人
    pub_date = models.DateTimeField() #发布日期


