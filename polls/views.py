from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html')

def detail(request, question_id):
    return HttpResponse(f"Вы находитесь на вопросе {str(question_id)}")
    

def result(result, question_id):
    return HttpResponse(f"Вы находитесь на результатах вопросе {str(question_id)}")
    

def vote(result, question_id):
    return HttpResponse(f"Вы проголосовали за вопрос №{str(question_id)}")
