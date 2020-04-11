from django.contrib import admin
from .models import SalesItem

@admin.register(SalesItem)
class SalesItemAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'title', 'sales_person', 'sales_amount'
    )