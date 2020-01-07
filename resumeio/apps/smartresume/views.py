from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import (
    ListView, DetailView, TemplateView, CreateView, View
    )
from .models import TemplateCategory, ResumeTemplate, PersonalDetails
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PersonalDetailsForm

class ResumeTemplateView(ListView):
    """
    Handle functions of displaying resume templates and their categories
    """
    template_name = 'resume_templates/resume_templates_list.html'
    context_object_name = 'templates'
    model = ResumeTemplate
    
    def get_context_data(self, **kwargs):
        """
        This method retrieves both resume templates and their categories
        """
        context =  super().get_context_data(**kwargs)
        categories = TemplateCategory.objects.all()
        context['categories'] = categories
        return context

    def get_absolute_url(self):
        reverse('smart_resume:create-resume', args = [self.name])


class CreateResumeView(LoginRequiredMixin, ListView):
    template_name = 'resumes/new_or_edit.html'
    context_object_name = 'template'
    model = ResumeTemplate
    login_url = '/auth/login/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ResumeDashboardView(TemplateView):
    template_name = 'home.html'


class DashboardView(TemplateView):
    template_name = 'resumes/resume_dashboard.html'


class PersonalDetails(View):
    """
    This view handles the functionality of saving user personal details to be added on their resumes. This is more of a user profile with limited details.
    """

    model = PersonalDetails
    form_class = PersonalDetailsForm
    
    def post(self, request):
        data = self.request.POST

        """
        Here, we need to add the authenticated user to the formclass.
        Since the request dictionary data is immutable, 
        we convert it to a mutable dictionary, add our new user field and 
        revert it back to its immutable state.
        """
        _mutable = data._mutable
        data._mutable = True
        user = self.request.user.id
        data['user'] = user
        data._mutable = _mutable

        personal_details_form = PersonalDetailsForm(data)
        if(personal_details_form.is_valid()):
            personal_details_form.save()
        
        return redirect('smart_resume:personal_details')
