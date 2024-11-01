from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PISU_Auth.urls')),  # Login como página principal
    #path('foro/', include('PISU_Foro.urls')),
    #path('anuario/', include('PISU_Anuario.urls')),
]

# Solo para desarrollo (sirve archivos estáticos)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])