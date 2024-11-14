from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_discusiones, name='lista_discusiones'),
    path('crear/', views.crear_discusion, name='crear_discusion'),
    path('<int:discusion_id>/', views.ver_discusion, name='ver_discusion'),
    path('<int:discusion_id>/publicar/', views.crear_publicacion, name='crear_publicacion'),
    path('publicacion/<int:publicacion_id>/comentar/', views.crear_comentario, name='crear_comentario'),
]
