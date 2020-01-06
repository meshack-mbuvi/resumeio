from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from .forms import SignUpForm
from django.contrib.auth import login

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        return render(request, 'registration/signup.html', {'form':form})
