from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.
#
def index(request):

    return render(request, 'polls/index.html')


def list_question(request):
    # question = get_object_or_404(Question,pk=1)
    question = Question.objects.all()
    context = {'dsquest': question}
    return render(request, 'polls/list_question.html', context)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail_question.html', {'qs': q})


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST['choice']
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse('Khong co choice')
    c.votes = c.votes + 1
    c.save()
    return render(request, 'polls/result.html', {'q': q})
