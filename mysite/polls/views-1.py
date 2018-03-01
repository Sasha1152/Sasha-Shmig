from django.http import HttpResponse, Http404
from . models import Question, Choice
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # return HttpResponse(', '.join([q.question_text for q in latest_question_list])) #2 remove
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list}) #2 add


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id) #2 remove
    # 3 remove:
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id) #3 add
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
