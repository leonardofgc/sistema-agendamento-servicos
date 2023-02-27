from django.db import models

# Create your models here.


class Agendamento(models.Model):

    def __str__(self) -> str:
        return f"{self.nome_cliente}"

    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length=200)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20)