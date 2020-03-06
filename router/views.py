from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def routerv(request):
    return HttpResponse("router hell")