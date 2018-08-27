from django.contrib import admin
from pip._internal.commands import search

from .models import Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    model = Pessoa
    list_display = ['nome', 'cpf', 'email']
    search_fields = ['nome']

admin.site.register(Pessoa, PessoaAdmin)

