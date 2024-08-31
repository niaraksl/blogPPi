from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='media/', blank=True, null=True)
    descricao = models.TextField()
    observacoes = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo