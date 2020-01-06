from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.shortcuts import redirect


def Home(request):
    return redirect('/dashboard')

class DashboardView(TemplateView):
    template_name = 'home.html'


