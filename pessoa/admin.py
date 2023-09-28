from django.contrib import admin
from pessoa.models import Pessoa

class Pessoas(admin.ModelAdmin):
    list_display =('nome', 'data_nascimento', 'endereco', 'cpf', 'estado_civil')
    list_display_links = ('nome', 'endereco')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Pessoa, Pessoas)