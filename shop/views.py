from django.shortcuts import render


def shop_view(request):
    return render(request, 'shop/shop.html', {})
    # 現在還沒有資料要從 model 傳給頁面
    # 所以 context 留空





# 之前練習用的code
# from django.http import JsonResponse, HttpRequest
# from django.views.decorators.csrf import csrf_exempt
# from django.core.handlers.wsgi import WSGIRequest
#
# import json
#
# from .forms import PostForm
# from .models import Post
#
#
# # 讓這支 API 免 csrf authentication
# # (之後我們再來深入!)
# @csrf_exempt
# def test_json_response_view(request: WSGIRequest):
#     print('-------------------------------')
#     if request.method == "GET":
#         print("get GET request: ", request)
#         return JsonResponse({'first': 'content', 'second': 'test'})
#     elif request.method == "POST":
#         # get json data
#         data = json.loads(request.body)
#         print("get POST request data: ", data)
#
#         # save to db
#         Post.objects.create(title=data['title'], content=data['content'])
#
#         # check posts in db
#         print('all post in db:', Post.objects.all())
#
#         # send response to client
#         return JsonResponse({'status': 'ok, I got u.'})
#     else:
#         print("Get unknown request: ", request)
#         return JsonResponse({'status': 'no, I don\'t know it.'})
#
#
# # 這次我們試著接受 Form 的 POST
# # 收到的 form 如果合法，我們就存到 DB 去
# def post_create_view(request):
#     form = PostForm(request.POST or None)
#     print("form valid: ", form.is_valid, ", request: ", request)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/post_create.html', context)
#
#
# # Create your views here.
# def hello(request):
#     context = {
#         "first_var": "Hello Man",   # 所謂框架：string, float -> context
#         "second_var": 8787.87,      # 再透過template engine 將其傳給index.html
#         "third_list": ['YY', 'BS', 'EL', 'SQ'],
#         "four_list": ["YY", "你好", "我是 RS", "來比對我阿"]
#     }
#     # 已經設定讀取templates了，所以可直接blog/index.html 就好
#     return render(request, 'blog/index.html', context)