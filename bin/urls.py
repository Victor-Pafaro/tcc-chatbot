# url - view - template

from django.urls import path, include
from .views import login, Homebin, Cadastro,DuvidasFrequentes

from django.contrib.auth import views as auth_view

app_name = 'bin'

urlpatterns = [
    path("", login),
    path("homepage/", Homebin.as_view()),
    path("logout/", auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('duvidasfrequentes/', DuvidasFrequentes.as_view(), name='duvidasfrequentes'),
]
