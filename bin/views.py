from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pergunta


# def login(request):
#     return render(request, "login.html")

class TelaInicial(TemplateView):
    template_name = "telainicial.html"

class Homebin(LoginRequiredMixin,TemplateView):
    template_name = "homebin.html"

class Cadastro(TemplateView):
    template_name = "cadastro.html"

class DuvidasFrequentes(LoginRequiredMixin,ListView):
    template_name = "duvidasfrequentes.html"
    model = Pergunta

