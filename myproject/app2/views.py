from django.shortcuts import render

# Create your views here.

def home_app2(request):
    return render(request, 'app2.html')