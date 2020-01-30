from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.api.serializers import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.models import Endereco
from pontos_turisticos.models import Atracao


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    #queryset = PontoTuristico.objects.all()
    filter_fields = ('nome', 'id',)

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)
        queryset = PontoTuristico.objects.filter(nome=nome)
        return queryset

    @action(methods=['post'], detail=True)
    def associa_endereco(self, request, pk):
        atracoes = request.data['id']

        ponto = PontoTuristico.objects.get(id=pk)

        ponto.atracoes.set(atracoes)

        return HttpResponse('ok')