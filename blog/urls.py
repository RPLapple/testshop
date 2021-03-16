from django.urls import path
# from . import views
from blog.views import hello

app_name = 'blog'
urlpatterns = [
    path('', hello),
]

# http://127.0.0.1:8000/polls/specifics/1
# path('specifics/<int:question_id>/', views.detail, name='detail'),

# index  : http://127.0.0.1:8000/polls/
# detail : http://127.0.0.1:8000/polls/1
# results:
# vote   :


# urlpatterns += staticfiles_urlpatterns()