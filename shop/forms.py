from django import forms
from .models import Post


# 透過 views.py 把 form 包在 context 傳給 html，
# 就可以在 html 上，呈現出我們想要讓使用者填的欄位
# 讓使用者填寫的欄位（作者、建立時間、發佈時間，不是讓使用者自己填的
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']