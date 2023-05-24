from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('register_success', views.RegisterSucces.as_view(), name='register_success'),
]
