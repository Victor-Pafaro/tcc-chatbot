from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


# class FormLogin(forms.Form):
#     ra = forms.CharField(label="RA", max_length=5)

class CriarContaForm(UserCreationForm):
    #ra = forms.IntegerField()
    email = forms.EmailField()
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':''})
    )
    password1 = forms.CharField(
        label="Senha",
        widget = forms.TextInput(attrs={'placeholder':''})
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')