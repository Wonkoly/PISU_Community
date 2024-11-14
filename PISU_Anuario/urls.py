from django.urls import path
from .views import anuario_view

urlpatterns = [
    path('', anuario_view, name='anuario'),
]
