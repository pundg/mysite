from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Welcome(request):
    return HttpResponse("hello welcome the Mywebsite")