from django.shortcuts import render,redirect, reverse
from .models import Pergunta
from .forms import CriarContaForm#, FormLogin
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


# def login(request):
#     return render(request, "login.html")

# class Teste(FormView):
#     template_name = "teste.html"
#     #form_class = FormLogin

class TelaInicial(TemplateView):
    template_name = "telainicial.html"

class Homebin(LoginRequiredMixin,TemplateView):
    template_name = "homebin.html"

class Cadastro(FormView):
    template_name = "cadastro.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bin:login')

class DuvidasFrequentes(LoginRequiredMixin,ListView):
    template_name = "duvidasfrequentes.html"
    model = Pergunta

