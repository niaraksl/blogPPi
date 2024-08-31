from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'idade', 'data_nascimento', 'foto', 'descricao', 'observacoes', 'data_cadastro')
    list_filter = ('data_cadastro', 'idade')
    search_fields = ('nome', 'email')
    date_hierarchy = 'data_cadastro'
    ordering = ('-data_cadastro', 'nome')
    fields = ('nome', 'email', 'idade', 'data_nascimento', 'foto', 'descricao', 'observacoes', 'data_cadastro')
    readonly_fields = ('data_cadastro',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'imagem','data_criacao')
    list_filter = ('data_criacao',)
    search_fields = ('titulo',)
    date_hierarchy = 'data_criacao'
    ordering = ('-data_criacao', 'titulo')
    fields = ('titulo', 'conteudo','imagem', 'data_criacao')
    readonly_fields = ('data_criacao',)