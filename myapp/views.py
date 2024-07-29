from django.shortcuts import render, get_object_or_404
from .models import Item

# View for listing items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

# View for a single item detail
def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'myapp/item_detail.html', {'item': item})



