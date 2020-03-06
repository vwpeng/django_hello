from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 这是第第三次测试
def index(request):
    # print("hello world")
    return HttpResponse("hello django 用DJANGO创建的第一个应用")


def hello(request):
    return HttpResponse('users hello')
