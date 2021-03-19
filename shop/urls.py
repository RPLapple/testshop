from django.urls import path
from shop.views import shop_view, product_view, \
    about_view, cart_view, checkout_view, \
    insert_view, lookup_view, modify_view, delect_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
    path('shop/', shop_view),
    path('product/', product_view),
    path('about/', about_view),
    path('cart/', cart_view),
    path('checkout/', checkout_view),
    path('insert/', insert_view),
    path('lookup/', lookup_view),
    path('modify/', modify_view),
    path('delete/', delect_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 今日重點，是我們能夠讀取到圖片的關鍵
# # 將存取路徑正確地導到圖片存放的路徑
# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
# )



# from . import views
# from .views import hello, post_create_view, test_json_response_view
# path('create/', post_create_view),        # 刪除舊的練習檔
# path('test/', test_json_response_view)    # 刪除舊的練習檔

# http://127.0.0.1:8000/polls/specifics/1
# path('specifics/<int:question_id>/', views.detail, name='detail'),

# index  : http://127.0.0.1:8000/polls/
# detail : http://127.0.0.1:8000/polls/1
# results:
# vote   :


# urlpatterns += staticfiles_urlpatterns()