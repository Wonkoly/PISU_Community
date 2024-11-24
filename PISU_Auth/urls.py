from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup_view, CustomLoginView, perfil_view, configuracion_view, verify_email, signup_success

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path("signup/", signup_view, name="signup"),
    path('verify/<int:user_id>/', verify_email, name='verify_email'),
    path('signup/success/', signup_success, name='signup_success'),
    path('perfil/', perfil_view, name='perfil'),
    path('configuracion/', configuracion_view, name='configuracion'),
]
