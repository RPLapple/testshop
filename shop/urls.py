from django.contrib import admin
from django.urls import path

from shop.views import shop_view
# from . import views
# from .views import hello, post_create_view, test_json_response_view

app_name = 'shop'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_view),
    # path('create/', post_create_view),        # 刪除舊的練習檔
    # path('test/', test_json_response_view)    # 刪除舊的練習檔
]

# http://127.0.0.1:8000/polls/specifics/1
# path('specifics/<int:question_id>/', views.detail, name='detail'),

# index  : http://127.0.0.1:8000/polls/
# detail : http://127.0.0.1:8000/polls/1
# results:
# vote   :


# urlpatterns += staticfiles_urlpatterns()