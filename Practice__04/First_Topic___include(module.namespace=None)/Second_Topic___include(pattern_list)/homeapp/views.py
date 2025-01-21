from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. & one functions 
def homeapp(request):
    return HttpResponse("First in homeapp")