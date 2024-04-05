from django.contrib import admin
from .models import  OrderModel

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "price",
        "date",
    )

    def save_model(self, request, obj, form, change):
        if not obj.price:
            products = form.cleaned_data.get('products') 
            total_price = sum(product.price * product.quantity for product in products)
            obj.price = total_price
        super().save_model(request, obj, form, change)
