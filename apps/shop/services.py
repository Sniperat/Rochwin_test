from django.db.models import Sum
from apps.employee.models import EmployeeModel
from apps.client.models import ClientModel

from .models import OrderModel


def get_employee_statistics(employee: EmployeeModel, year, month):
    queryset_params = {
        'employee': employee 
    }
    if month:
        queryset_params['date__month'] = month
    if year:
        queryset_params['date__year'] = year
    orders = OrderModel.objects.filter(**queryset_params)

    total_clients = orders.values('client').distinct().count()
    total_products_sold = orders.aggregate(total_products=Sum('products__quantity'))['total_products']
    total_sales = orders.aggregate(total_sales=Sum('price'))['total_sales']

    return {
        'full_name': employee.full_name,
        'total_clients': total_clients,
        'total_products_sold': total_products_sold,
        'total_sales': total_sales
    }

def get_all_employees_statistic(year, month):
    employees = EmployeeModel.objects.all()
    employee_stats = []
    queryset_params = {}
    if month:
        queryset_params['date__month'] = month
    if year:
        queryset_params['date__year'] = year
    for employee in employees:
        orders = OrderModel.objects.filter(employee=employee, **queryset_params)
        total_clients = orders.values('client').distinct().count()
        total_products_sold = orders.aggregate(total_products=Sum('products__quantity'))['total_products']
        total_sales = orders.aggregate(total_sales=Sum('price'))['total_sales']

        employee_stats.append({
            'id': employee.id,
            'full_name': employee.full_name,
            'total_clients': total_clients,
            'total_products_sold': total_products_sold,
            'total_sales': total_sales
        })
    return employee_stats


def get_client_statistics(client: ClientModel, year, month):
    queryset_params = {
        'client': client 
    }
    if month:
        queryset_params['date__month'] = month
    if year:
        queryset_params['date__year'] = year
    orders = OrderModel.objects.filter(**queryset_params)

    total_products_bought = orders.aggregate(total_products=Sum('products__quantity'))['total_products']
    total_sales = orders.aggregate(total_sales=Sum('price'))['total_sales']

    return {
        'id': client.id,
        'full_name': client.full_name,
        'total_products_bought': total_products_bought,
        'total_sales': total_sales
    }