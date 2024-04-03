from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя продукта')
    quantity  = models.IntegerField(default=0, verbose_name='количество в наличии')
    price = models.FloatField(default=0, verbose_name='цена')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
