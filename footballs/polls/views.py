from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"polls/index.html")

def question(request):
    return HttpResponse("1111111111")
