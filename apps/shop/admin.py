from django.contrib import admin
from .models import  OrderModel

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "price",
        "date",
    )