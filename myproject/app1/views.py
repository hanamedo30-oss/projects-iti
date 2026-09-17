from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

# 1. READ & INSERT (عرض البيانات وإضافتها)
def home_app1(request):
    if request.method == 'POST':
        item_name = request.POST.get('name')
        item_desc = request.POST.get('description')
        if item_name and item_desc:
            Item.objects.create(name=item_name, description=item_desc)
            return redirect('home_app1')

    items = Item.objects.all()
    return render(request, 'app1.html', {'items': items})

# 2. UPDATE (تعديل عنصر)
def update_item_app1(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('home_app1')
    return render(request, 'update_app1.html', {'item': item})

# 3. DELETE (حذف عنصر)
def delete_item_app1(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('home_app1')