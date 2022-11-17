from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    name = "Phạm Quốc Hoàng"
    address = "Quảng Ngãi"
    phone = 123456789
    courses = ["Python","PHP","Java","Html"]
    result = {"name":name,"address":address,"phone":phone,"courses":courses}
    return render(request,"polls/index.html",result)
