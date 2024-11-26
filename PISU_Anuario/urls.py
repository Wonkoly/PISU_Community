from django.urls import path
from . import views

urlpatterns = [
    path('', views.anuario, name='anuario'),
    path('agregar/', views.agregar_foto, name='agregar_foto'),
    path('<int:foto_id>/', views.ver_foto, name='ver_foto'),
    path('<int:foto_id>/editar/', views.editar_foto, name='editar_foto'),
    path('<int:foto_id>/eliminar/', views.eliminar_foto, name='eliminar_foto'),
    path('<int:foto_id>/compartir/', views.compartir_foto, name='compartir_foto'),
]