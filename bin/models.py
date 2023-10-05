from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Pergunta(models.Model):
    descricao_pergunta = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao_pergunta

#user
class Usuario(AbstractUser):
   ra = models.IntegerField(default=0)