from django.contrib import admin
from .models import ClientModel

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "full_name",
        "birth_date",
        "created_at",
    )
