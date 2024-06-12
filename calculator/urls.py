from django.urls import path
from .views import calculate_mortgage, calculate_principal_limit

urlpatterns = [
    path('', calculate_mortgage, name='calculate_mortgage'),
    path('calculate/', calculate_principal_limit, name='calculate_principal_limit'),
]
