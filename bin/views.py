from django.shortcuts import render,redirect, reverse
from .models import Pergunta
from .forms import CriarContaForm, FormHomebin
from django.views import View
from django.http import JsonResponse
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .chat import Chat

class TelaInicial(TemplateView):
    template_name = "telainicial.html"


class Homebin(LoginRequiredMixin, View):
    template_name = "homebin.html"
    form_class = FormHomebin

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            chat = Chat()
            chat.treino()

            valor_digitado = form.cleaned_data['pergunta']
            chat.pergunta = valor_digitado

            resposta = chat.get_resposta()
            if not resposta:
                print('Desculpe essa pergunta não está em meu escopo de conhecimento')
                return JsonResponse({'resposta': 'Desculpe, essa pergunta não está em meu escopo de conhecimento'})

            print(resposta)

            data = {'resposta':str(resposta)}

            return JsonResponse(data)

        return JsonResponse({'resposta': 'Erro no formulário'}, status=400)

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