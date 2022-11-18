from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
# Create your views here.


def index(request):
    name = "Phạm Quốc Hoàng"
    address = "Quảng Ngãi"
    phone = 123456789
    courses = ["Python","PHP","Java","Html"]
    result = {"name":name,"address":address,"phone":phone,"courses":courses}
    return render(request,"polls/index.html",result)

def view_question(request):
    question_list = Question.objects.all()
    # question_list_1 = Question.objects.filter(id = 1).first()
    
    result = {"question_list":question_list}
    # result['question_list_1'] = question_list_1

    return render(request,"polls/view_question.html",result)

def view_choice(request):
    choice_list = Choice.objects.all()
    result = {"choice_list":choice_list}
    return render(request,"polls/view_choice.html",result)


def detai_question(request,question_id):
    detail_question = Question.objects.get(pk=question_id)
    return render(request,"polls/detai_question.html",{"detail_question":detail_question})

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk = data)
    except:
        HttpResponse("Error: Không có data!")
    c.choice_vote = c.choice_vote + 1
    c.save()
    return render(request,"polls/result.html",{"q":q})