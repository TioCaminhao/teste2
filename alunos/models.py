from django.db import models
from django import forms

# Create your models here.

class Servicos (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class FormServicos (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.IntegerField()
    servico = models.ForeignKey(Servicos, on_delete= models.CASCADE)
    detalhes = models.TextField()
    data = models.DateField()
    aceita = models.BooleanField(default=None, null=True)  # None para representar um estado inicial

    def __str__(self):
        status = "Aceita" if self.aceita else "Negada" if self.aceita is False else "Pendente"
        return f"{self.nome} e {status}"