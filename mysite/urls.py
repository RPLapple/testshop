"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls', namespace='polls')),
    path('', include('shop.urls', namespace='shop')),
]


# path(route, view, kwargs, name)
# route : 匹配url的項
# view  : 調用特定views
# kwargs: 任意個關鍵自參數可以作為一個字典傳遞給目標view函數
# name  : 為url取名，可使你在Django的任意地方唯一地引用他