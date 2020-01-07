from django.urls import path
from .views import (
    DashboardView, ResumeTemplateView, CreateResumeView, PersonalDetails,ResumeDashboardView
)

app_name = 'smart_resume'
urlpatterns = [
    path('', ResumeDashboardView.as_view(), name = 'dashboard'),
    path('resumes/', DashboardView.as_view(), name = 'resumes'),
    path('resumes/new/', CreateResumeView.as_view(), name = 'new-resume'),
    path('resumes/personal_details', PersonalDetails.as_view(), name='personal_details' )
]
