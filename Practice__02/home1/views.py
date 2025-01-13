from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. & multiple functions 
def newapp(request):
    return HttpResponse("Hello Django Deverlopers")

def newapp1(request):
    return HttpResponse("<h1> Hello Django Deverlopers </h1>")

def newapp2(request):
    a = "<h3> Hello Django Deverlopers </h3>"
    return HttpResponse(a)

def newapp3(request):
    total = 101 + 202
    return HttpResponse("Hello Django Deverlopers",total)