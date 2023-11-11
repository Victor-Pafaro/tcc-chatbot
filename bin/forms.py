from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms



class FormHomebin(forms.Form):
     pergunta = forms.CharField(label=False,widget = forms.TextInput(attrs={'placeholder':'Digite sua dúvida...'}))

class CriarContaForm(UserCreationForm):
    #ra = forms.IntegerField()
    email = forms.EmailField()
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':''})
    )
    password1 = forms.CharField(
        label="Senha",
        widget = forms.PasswordInput(attrs={'placeholder':''})
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')