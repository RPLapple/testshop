from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # null=True
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now()
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    # 加上發布時間，並且存到 db 裡
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # now = timezone.now()
        # self.published_date = now + 1  # 好像沒跑出來
        # self.save()

    def __str__(self):
        return self.title
# 1. 新增一個model後，需到blog/admin.py去註冊才會生效
# 2. 且每次更改model後，都要makemigrations和migrate。
