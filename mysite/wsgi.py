"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Django 利用 DJANGO_SETTINGS_MODULE 环境变量来定位合适的配置模块。
# 它必须包含到配置模块的点式路径。开发环境和生产环境可以配置不同值；这都取决于你是如何组织配置的。
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# 用 WSGI 部署的关键是 application callable，应用服务器用它与你的代码交互。
application = get_wsgi_application()

# WSGI 服务器从其配置中获取 application callable 的路径。
# Django 的默认服务器（ runserver 命令），从配置项 WSGI_APPLICATION 中获取。
# 默认值是 <project_name>.wsgi.application，
# 指向 <project_name>/wsgi.py 中的 application callable。
