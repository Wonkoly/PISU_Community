from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from PISU_Community import views

urlpatterns = [
    path('', views.index, name='index'),  # Login como página principal
    path('admin/', admin.site.urls),
    path('auth/', include('PISU_Auth.urls')),  # Login como página principal 
    path('foro/', include('PISU_Foro.urls')),
    path('anuario/', include('PISU_Anuario.urls')),
    path('buscar/', views.buscar, name='buscar'),  # Buscador global
]

# Solo para desarrollo (sirve archivos estáticos)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)