from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Carrera, CentroUniversitario

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol', 'carrera', 'centro_universitario')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Carrera)
admin.site.register(CentroUniversitario)
