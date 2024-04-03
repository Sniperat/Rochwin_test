from django.contrib import admin
from .models import EmployeeModel

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "full_name",
        "birth_date",
        "created_at",
    )
