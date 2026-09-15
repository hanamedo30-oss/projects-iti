from django.shortcuts import render

# Create your views here.

def home_app1(request):
    return render(request, 'app1.html')