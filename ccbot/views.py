from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(content='<h1>Hello, Welcome</h1>')

def signup(request):
    return HttpResponse(content='<h1>Hello, this is the register page</h1>')

def signin(request):
    return HttpResponse(content="This is the Sign in page")