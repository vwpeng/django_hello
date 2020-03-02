from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
#
def index(request):
    # print("hello world")
    return HttpResponse("hello django 用DJANGO创建的第一个应用")
