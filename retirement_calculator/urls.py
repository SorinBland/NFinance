from django.urls import path

from retirement_calculator.views import retirement_calculator

urlpatterns = [
    path('', retirement_calculator, name='calculator')
]
