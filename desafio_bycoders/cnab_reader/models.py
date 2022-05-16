from django.db import models
from .models_validators import validate_transaction


# Create your models here.



class cnabModel(models.Model):
    tipo_transacao = models.IntegerField(validators=[validate_transaction], blank=False, null=False)	
    data = models.DateField(blank=False, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    cartao = models.CharField(max_length=12, blank=False, null=False)
    hora_transacao = models.TimeField(blank=False, null=False)
    nome_dono_loja = models.CharField(max_length=14, blank=False, null=False)
    nome_loja = models.CharField(max_length=19, blank=False, null=False)


    def __str__(self):
        return self.nome_loja

    def __repr__(self):
        return self.nome_loja




