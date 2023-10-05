from django.shortcuts import render,redirect, reverse
from .models import Pergunta
from .forms import CriarContaForm, FormHomebin
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

class Homebin(LoginRequiredMixin,FormView):
    template_name = "homebin.html"
    form_class= FormHomebin

    def get_success_url(self):
        pergunta = self.request.POST.get("pergunta") # Pega a pergunta
        perguntas = Pergunta.objects.filter(descricao_pergunta=pergunta) #Verifica se a pergunta feita é a mesma que tem no campo de descrição pergunta no banco de dados.
        # Fazer a parte da API aqui, por enquanto se a pergunta feita for igual a descrição pergunta que tem no banco vai levar a pessoa pra pagina de login.
        if perguntas:
            return reverse('bin:perguntacerta')
        else:
            return reverse('bin:perguntaerrada')


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

class PerguntaCerta(TemplateView):
    template_name = "perguntacerta.html"

class PerguntaErrada(TemplateView):
    template_name = "perguntaerrada.html"