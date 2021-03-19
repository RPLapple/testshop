from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
import json
import random

from .models import Product


def delect_view(request):
    product = Product.objects.get(id=1)
    product.delete()
    return HttpResponse('刪除 id=1 的資料成功，請到 SQL shell 下指令\nsql> select * from product')


def modify_view(request):
    product = Product.objects.get(id=1)
    product.name = "我是後來才修改的產品"
    product.save()
    return HttpResponse('修改完成，到Mongo Compass確認資料')


def lookup_view(request):
    result = Product.objects.all()
    mlist = []
    for item in result:
        content = {"product name": item.name, "price": float(item.price)}
        mlist.append(content)
    return HttpResponse(mlist)


def insert_view(request):
    for i in range(5):
        product = Product()
        product.name = "測試" + str(random.randint(0, 5))
        product.price = random.randint(1, 500)
        product.save()
    return HttpResponse("批次新增資料完成")


# 在 views.py 拿到存放在資料庫的 Product 資料，
# 包成 context 再傳給 html，
# html 再把產品資訊拆開，放到各個地方。
def shop_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg',
        # 將 QuerySet 轉成 list
        # 以 context 的方式傳給 templates
        'products': list(Product.objects.all())
    }
    return render(request, 'shop/shop.html', context)
    # 現在還沒有資料要從 model 傳給頁面
    # 所以 context 留空


def product_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg'
    }
    return render(request, 'shop/product-single.html', context)


def about_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg',
        'bg_2': '/static/images/bg_2.jpg',
        'bg_4': '/static/images/bg_4.jpg',
        'person_1': '/static/images/person_1.jpg',
        'person_2': '/static/images/person_2.jpg',
        'person_3': '/static/images/person_3.jpg',
    }
    return render(request, 'shop/about.html', context)


def cart_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg',
        'product_3': '/static/images/product_3.jpg',
        'product_4': '/static/images/product_4.jpg',
    }
    return render(request, 'shop/cart.html', context)


def checkout_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg',
    }
    return render(request, 'shop/checkout.html', context)




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