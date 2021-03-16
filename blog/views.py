from django.shortcuts import render


# Create your views here.
def hello(request):
    context = {}
    return render(request, 'templates/blog/index.html', context)