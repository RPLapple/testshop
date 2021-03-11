# 如果指定问题 ID 所对应的问题不存在，这个视图就会抛出一个 Http404 异常
# from django.http import Http404
# from django.http import HttpResponse 被render取代
# from django.template import loader   被render取代
# render() 载入模板，填充上下文，再返回由它生成的 HttpResponse 对象
# get_object_or_404(): 尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误
# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):          # ListView: 顯示一個對象列表
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):       # DetailView: 顯示一個特定類對象的詳細信息頁面
    model = Question                        # DV: 期望從URL中捕獲pk值 -> question_id ->pk
    template_name = 'polls/detail.html'     # <app name>/<model name>_detail.html

    # 就算在发布日期时，未来的投票不会在目录页 index里出现，
    # 但是如果用户知道或者猜到正确的URL，还是可以访问到它。所以得在 DetailView 里增加一些约束：
    # Excludes any questions that aren't published yet.
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    # return HttpResponse("You're voting on question %s." % question_id)

    # request.POST
    # 类字典对象，让你可以通过关键字的名字获取提交的数据
    # +['choice']:以字符串形式返回选择的Choice的ID。
    # 值永远是字符串
    # 保证数据只能通过POST调用改动
    # 如果在 request.POST['choice'] 数据中没有提供 choice ， POST 将引发一个 KeyError

    # HttpResponseRedirect
    # 增加 Choice 的得票数之后，代码返回 HttpResponseRedirect 而不是常用的 HttpResponse
    # HRR 只接收一个参数：用户将要被重定向到的 URL

    # reverse
    # 在 HttpResponseRedirect 的构造函数中使用 reverse() 函数。
    # 避免我们在视图函数中硬编码 URL


# 整段刪除換成上面的class blablabla
# Create your views here.
# def index(request):   # http://127.0.0.1:8000/polls/
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)


# # 3 是 question.id 的值。重定向的 URL 将调用 'results' 视图来显示最终的页面。
# # http://127.0.0.1:8000/polls/3/results/
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)