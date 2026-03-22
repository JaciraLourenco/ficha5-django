from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.CharField(max_length=300)

    def __str__(self):
        return self.texto

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='opcoes')
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class Resultado(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resultados')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='resultados')
    pontuacao = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilizador} - {self.quiz} - {self.pontuacao}"
