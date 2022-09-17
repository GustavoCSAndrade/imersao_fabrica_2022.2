
from django.shortcuts import render, redirect
from .forms import FormularioPostagem



# Create your views here.

from django.shortcuts import render
from .models import PostagemLigações

def home(request):
    ligacoes = PostagemLigações.objects.all()
    data={}
    data['ligacoes'] = ligacoes

    return render(request, 'blog/home.html', data)

def create(request):
    form = FormularioPostagem(request.POST or None)
    data = {}
    data['form'] = form
    
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'blog/create.html',data)

def leitura_postagem(request, pk):
    ligacoes = PostagemLigações.objects.get(pk=pk)
    data = {}
    data['ligacoes'] = ligacoes

    return render(request, 'blog/post.html', data)
    
def update(resquest, pk):
    ligacoes = PostagemLigações.objects.get(pk=pk)
    form = FormularioPostagem(request.POST or None, instance = post)
    data = {}
    data['ligacoes'] = ligacoes

    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'blog/update.html',data)

def delete(request, pk):
    postagem = PostagemLigações.objects.get(pk=pk)
    postagem.delete()

    return redirect('home')

  
