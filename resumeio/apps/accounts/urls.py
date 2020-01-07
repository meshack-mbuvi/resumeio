from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('login/', auth_views.LoginView.as_view(), name = 'login')
]
