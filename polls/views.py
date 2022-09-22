from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'latest_question_list': questions,
    }
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
    }
    return render(request, 'detail.html', context)
    

def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
    }
    return render(request, 'result.html', context)
    

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice = question.choice_set.get(id=request.POST['choice'])
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('result', args=(question_id, )))
