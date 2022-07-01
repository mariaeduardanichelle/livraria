from unittest.util import _MAX_LENGTH
from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nomeate

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def__str__(self):
        return self.nome
    
class livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    

