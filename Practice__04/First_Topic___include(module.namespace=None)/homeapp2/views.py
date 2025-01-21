from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. & one functions 
def homeapp2(request):
    return HttpResponse("Second in homeapp2")