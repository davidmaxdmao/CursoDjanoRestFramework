from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Atrações'

    def __str__(self):
        return self.nome
