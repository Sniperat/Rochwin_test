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
    
    # @classmethod
    # def create(cls, client, employee, products, date):
    #     order = cls(client=client, employee=employee, date=date)
    #     order.save()

    #     total_price = sum(product.price * product.quantity for product in products)
    #     order.price = total_price
    #     order.save()

    #     return order
    
      
    def save(self, *args, **kwargs):
        super(OrderModel, self).save(*args, **kwargs)
        print(self.products)
        print(self.products.all())
        total_price = sum(product.price * product.quantity for product in self.products.all())
        print(total_price)
        self.price = total_price
        super(OrderModel, self).save(*args, **kwargs)

# import datetime
# my_client = ClientModel.objects.get(pk=1)
# my_employee = EmployeeModel.objects.get(pk=1)
# my_products = [ProductModel.objects.get(pk=1), ProductModel.objects.get(pk=2)]
# my_date = datetime.date.today()

# # Создание заказа с использованием пользовательского метода create
# order = OrderModel.objects.create(client=my_client, employee=my_employee, products=my_products, date=my_date)