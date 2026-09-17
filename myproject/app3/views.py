from django.shortcuts import render

# Create your views here.


def home_app3(request):
    return render(request, 'app3.html')