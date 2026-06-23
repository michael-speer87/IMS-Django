from django.db import models

class InventoryItem(models.Model):
    # Core Asset Information
    item_name = models.CharField(max_length=200, verbose_name="Item Name")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Serial Number")
    location = models.CharField(max_length=200, verbose_name="Location")
    status = models.CharField(max_length=50, default='Inventory', verbose_name="Status")

    # Procurement / Vendor Data
    vendor_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Vendor Name")
    vendor_invoice_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Invoice Number")
    vendor_invoice_date = models.DateField(blank=True, null=True, verbose_name="Invoice Date")
    vendor_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Vendor Amount")

    # Deployment Log Details
    install_date = models.DateField(blank=True, null=True, verbose_name="Installation Date")
    work_order = models.CharField(max_length=100, blank=True, null=True, verbose_name="Work Order")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    def __str__(self):
        return F"{self.item_name} ({self.serial_number})"