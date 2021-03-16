from django.urls import path
from . import views

# 在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。
# Django 如何分辨重名的 URL 呢？
# + app_name = 'app名稱'
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# http://127.0.0.1:8000/polls/specifics/1
# path('specifics/<int:question_id>/', views.detail, name='detail'),

# index  : http://127.0.0.1:8000/polls/
# detail : http://127.0.0.1:8000/polls/1
# results:
# vote   :


# urlpatterns += staticfiles_urlpatterns()