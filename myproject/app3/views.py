from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_app3(request):
    return HttpResponse("<h1>Welcome to Application 3</h1>")