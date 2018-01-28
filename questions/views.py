#=AleX=
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

# Import our models from models.py
from .models import Question, Answer


def index(request):
	# return 10 latest questions
    return render(request, "index.html", {"latest_questions": Question.objects.order_by('-added_at')[:10]})


def detail(request, question_id):
    return render(request, "answer.html", {"question": get_object_or_404(Question, pk=question_id)})


def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'answer.html', {'question': question, 'error_message': request.POST['answer']})
    else:
        if answer.correct:
            return render(request, "index.html", {"latest_questions": Question.objects.order_by('-added_at')[:10], "message": "Right!"})
        else:
            return render(request, 'answer.html', {'question': question, 'error_message': 'Wrong!'})
