# PISU_Foro/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('<int:publicacion_id>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('nueva/', views.crear_publicacion, name='crear_publicacion'),
]
