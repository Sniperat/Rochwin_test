# Generated by Django 5.0.3 on 2024-04-03 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('employee', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='общая цена заказа')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='client.clientmodel', verbose_name='клиент')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='employee.employeemodel', verbose_name='сотрудник')),
                ('products', models.ManyToManyField(to='product.productmodel', verbose_name='продукты')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
