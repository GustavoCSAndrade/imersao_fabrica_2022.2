from django.forms import ModelForm
from .models import PostagemLigações

class FormularioPostagem(ModelForm):

    class Meta:
        models = PostagemLigações
        fields = ['tecnico','conteudo','tempoDeLigação']
       