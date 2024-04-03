from django.db import models
from apps.client.models import ClientModel
from apps.employee.models import EmployeeModel
from apps.product.models import ProductModel
        
        
class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.RESTRICT, verbose_name='клиент')
    employee = models.ForeignKey(EmployeeModel, on_delete=models.RESTRICT, verbose_name='сотрудник')
    products = models.ManyToManyField(ProductModel, verbose_name='продукты')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='общая цена заказа')
    
    date = models.DateField(auto_now_add=True, verbose_name='дата заказа')
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    