from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'PISU_Auth/login.html')

def signup_view(request):
    return render(request, 'PISU_Auth/signup.html')