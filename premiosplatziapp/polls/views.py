from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "Polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número{question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número{question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número {question_id}")


