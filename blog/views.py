from django.shortcuts import render


# Create your views here.
def hello(request):
    context = {
        "first_var": "Hello Man",   # 所謂框架：string, float -> context
        "second_var": 8787.87,      # 再透過template engine 將其傳給index.html
        "third_list": ['YY', 'BS', 'EL', 'SQ'],
        "four_list": ["YY", "你好", "我是 RS", "來比對我阿"]
    }
    # 已經設定讀取templates了，所以可直接blog/index.html 就好
    return render(request, 'blog/index.html', context)