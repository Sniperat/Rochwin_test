from django.urls import path
from .views import (
    SingleEmployeStatistic,
    AllEmployeesStatistics,
    ClientStatisticsView
)


urlpatterns = [
    path('statistics/employee/<int:pk>/', SingleEmployeStatistic.as_view()),
    path('employee/statistics/', AllEmployeesStatistics.as_view()),
    path('statistics/client/<int:pk>', ClientStatisticsView.as_view()),
    
]