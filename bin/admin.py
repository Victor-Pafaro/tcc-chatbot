from django.contrib import admin
from .models import Pergunta, Usuario
from django.contrib.auth.admin import UserAdmin

# Só existe pq queremos que no admin apareça o campo de RA do aluno
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Informação Escolar", {'fields': ('ra',)})
)

UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(Usuario,UserAdmin)

