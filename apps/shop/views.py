from datetime import datetime

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.employee.models import EmployeeModel
from apps.client.models import ClientModel

from . import services


class SingleEmployeStatistic(APIView):
    permission_classes = (AllowAny,)
    
    def get_object(self):
        obj = get_object_or_404(EmployeeModel, pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get(self, request, pk):
        month = int(request.query_params.get('month', False))
        year = int(request.query_params.get('year', False))
            
        result = services.get_employee_statistics(self.get_object(), year, month)
        
        return Response(data=result)
        

class AllEmployeesStatistics(APIView):
    def get(self, request, format=None):
        month = int(request.query_params.get('month', 1))
        year = int(request.query_params.get('year', datetime.now().year))

        result = services.get_all_employees_statistic(year, month)        

        return Response(result)
    

class ClientStatisticsView(APIView):
    permission_classes = (AllowAny,)
    
    def get_object(self):
        obj = get_object_or_404(ClientModel, pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get(self, request, pk):
        month = int(request.query_params.get('month', False))
        year = int(request.query_params.get('year', False))
            
        result = services.get_client_statistics(self.get_object(), year, month)
        
        return Response(data=result)