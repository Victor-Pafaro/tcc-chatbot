from django.contrib import admin
from .models import Pergunta#,Aluno
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Pergunta)
#admin.site.register(Aluno,UserAdmin)