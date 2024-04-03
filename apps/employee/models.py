from django.db import models


class EmployeeModel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    birth_date = models.DateField(verbose_name='дата рождения')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
