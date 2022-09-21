from django.shortcuts import render
from django.http import HttpResponse


def detail(request, question_id):
    return HttpResponse(f"Вы находитесь на вопросе {str(question_id)}")
    

def result(result, question_id):
    return HttpResponse(f"Вы находитесь на результатах вопросе {str(question_id)}")
    

def vote(result, question_id):
    return HttpResponse(f"Вы проголосовали за вопрос №{str(question_id)}")
