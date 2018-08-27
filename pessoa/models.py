# from django.db import models
from djongo import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    curriculo = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome