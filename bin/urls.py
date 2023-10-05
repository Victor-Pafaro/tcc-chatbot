# url - view - template

from django.urls import path, include
from .views import Homebin, Cadastro, DuvidasFrequentes, TelaInicial, PerguntaCerta, PerguntaErrada

from django.contrib.auth import views as auth_view

app_name = 'bin'

urlpatterns = [
    path("", TelaInicial.as_view(), name='telainicial'),
    path("login/", auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("homepage/", Homebin.as_view(), name='homebin'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('duvidasfrequentes/', DuvidasFrequentes.as_view(), name='duvidasfrequentes'),
    path('perguntacerta', PerguntaCerta.as_view(), name='perguntacerta'),
    path('perguntaerrada', PerguntaErrada.as_view(), name='perguntaerrada'),
]
