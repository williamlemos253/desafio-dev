from rest_framework import serializers
from cnab_reader.models import cnabModel
from django.db.models import Sum



class CnabSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = cnabModel
        fields = (
        'tipo_transacao',
        'data',
        'valor',
        'cpf',
        'cartao',
        'hora_transacao',
        'nome_dono_loja',
        'nome_loja',
        'total',
    )

    @classmethod
    def get_total(cls, instance):
        total = cnabModel.objects.all().aggregate(Sum('valor'))
        return total