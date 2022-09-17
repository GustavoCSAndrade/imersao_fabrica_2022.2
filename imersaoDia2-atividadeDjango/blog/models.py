from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class PostagemLigações(models.Model):
    tecnico = models.CharField(max_length=80)
    conteudo = models.TextField()
    tempoDeLigação = models.CharField(max_length=5)
    dataHora= models.DateTimeField(auto_now_add=True)
