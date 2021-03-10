from django.contrib import admin

from .models import Question

# Register your models here.
# 向管理页面注册了问题Question类。Django 知道它应该被显示在admin後台索引页里
admin.site.register(Question)