from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth import login
from .forms import SignUpForm

from django.core.exceptions import ValidationError

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm

    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
        

        return render(request, 'accounts/signup.html', {'form':form})

  