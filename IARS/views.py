from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .models import Accident
from .forms import AccidentForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class AccidentCreateView(FormView):
    form_class = AccidentForm
    template_name = 'accident/report/accident_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        accident = form.save(commit=False)
        accident.user = self.request.user
        accident.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseBadRequest()
    
def index(request):
    accidents = Accident.objects.all()
    context = {'accidents': accidents}
    return render(request, 'index.html', context)