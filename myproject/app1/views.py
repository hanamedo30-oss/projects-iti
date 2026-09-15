from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_app1(request):
    return HttpResponse("<h1>Welcome to Application 1</h1>")