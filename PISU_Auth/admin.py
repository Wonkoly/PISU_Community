from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CentroUniversitario, Carrera
from .forms import CustomUserCreationForm  # Usa solo el formulario para creación de usuarios

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # Solo usa el formulario para agregar usuarios

    list_display = ('username', 'email', 'rol', 'is_verified', 'anonimo')
    list_filter = ('rol', 'is_verified', 'anonimo')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'centro_universitario', 'carrera', 'foto_perfil')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Configuraciones', {'fields': ('anonimo', 'is_verified', 'rol')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'rol', 'is_verified', 'anonimo'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

class CentroUniversitarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(CentroUniversitario, CentroUniversitarioAdmin)

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'centro_universitario')
    list_filter = ('centro_universitario',)
    search_fields = ('nombre',)

admin.site.register(Carrera, CarreraAdmin)
