from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    pessoa = Pessoa.objects.all().first()
    posts = Post.objects.all()
    contexto = {
        'pessoa': pessoa,
        'posts': posts
        }
    return render(request, 'blogPPI/index.html', contexto)

def about(request):
    pessoa = Pessoa.objects.all().first()
    contexto = { 'pessoa': pessoa }
    return render(request, 'blogPPI/about.html', contexto)

def contact(request):
    pessoa = Pessoa.objects.all().first()
    contexto = { 'pessoa': pessoa }
    return render(request, 'blogPPI/contact.html', contexto)