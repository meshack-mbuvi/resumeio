from django.urls import path
from .views import DashboardView, Home

app_name = 'smart_resume'
urlpatterns = [
    path('', Home, name = 'home'),
    path('dashboard/', DashboardView.as_view(), name = 'dashboard'),
    path('dashboard/create-resume/', DashboardView.as_view(), name = 'create-resume')
]