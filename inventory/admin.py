from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    # Columns displayed in the dashboard list view
    list_display = ('item_name', 'serial_number', 'location', 'status', 'work_order', 'install_date')
    # Search Constraints
    search_fields = ('item_name', 'serial_number', 'work_order')
    # Quick Filter sidebars
    list_filter = ('status', 'location')