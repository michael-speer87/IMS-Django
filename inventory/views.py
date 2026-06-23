from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem
from .forms import InventoryItemForm

def inventory_list(request):
    # Fetch all items from the database, ordered by newest first
    items = InventoryItem.objects.all().order_by('-id')

    # Pass the items to the HTML template
    context = {
        'items': items
    }
    return render(request, 'inventory/inventory_list.html', context)

def add_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    
    return render(request, 'inventory/inventory_form.html', {'form': form})

def update_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)

    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm(instance=item)
    
    return render(request, 'inventory/inventory_form.html', {'form': form, 'is_update': True})

def delete_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    
    if request.method == 'POST':
        # If the user confirms the deletion via POST request, delete it
        item.delete()
        return redirect('inventory_list')
        
    # If they just navigated to the page, show them a confirmation screen
    return render(request, 'inventory/inventory_confirm_delete.html', {'item': item})