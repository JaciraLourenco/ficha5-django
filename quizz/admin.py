from django.contrib import admin

from django.contrib import admin
from .models import Quiz, Pergunta, Opcao, Resultado

admin.site.register(Quiz)
admin.site.register(Pergunta)
admin.site.register(Opcao)
admin.site.register(Resultado)
