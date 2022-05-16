from django.shortcuts import render
from cnab_reader.models import cnabModel
from .serializers import CnabSerializer
from django.db.models import Sum
from rest_framework import generics



class CnabReaderAPIView(generics.ListCreateAPIView):
    queryset = cnabModel.objects.all()
    serializer_class = CnabSerializer

    def get_queryset(self):
        if self.kwargs.get('nome_loja'):
            query_total_value = self.queryset.aggregate(Sum('valor'))
            query_total_value =  str(round(query_total_value['valor__sum'], 2))
            return self.queryset.filter(nome_loja=self.kwargs.get('nome_loja'))
        return self.queryset.all()
