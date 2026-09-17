from django.shortcuts import render, redirect, get_object_or_404
from .models import Item2

def home_app2(request):
    if request.method == 'POST':
        item_name = request.POST.get('name')
        item_desc = request.POST.get('description')
        if item_name and item_desc:
            Item2.objects.create(name=item_name, description=item_desc)
            return redirect('home_app2')

    items = Item2.objects.all()
    return render(request, 'app2.html', {'items': items})

def update_item_app2(request, item_id):
    item = get_object_or_404(Item2, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('home_app2')
    return render(request, 'update_app2.html', {'item': item})

def delete_item_app2(request, item_id):
    item = get_object_or_404(Item2, id=item_id)
    item.delete()
    return redirect('home_app2')