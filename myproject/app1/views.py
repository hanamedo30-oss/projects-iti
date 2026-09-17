from django.shortcuts import render, redirect
from .models import Item

def home_app1(request):
    # إضافة عنصر جديد عند استقبال طلب POST (إدخال بيانات)
    if request.method == 'POST':
        item_name = request.POST.get('name')
        item_desc = request.POST.get('description')
        if item_name and item_desc:
            Item.objects.create(name=item_name, description=item_desc)
            return redirect('/app1/')

    # جلب وقراءة جميع العناصر المجهزة من قاعدة البيانات
    items = Item.objects.all()
    return render(request, 'app1.html', {'items': items})