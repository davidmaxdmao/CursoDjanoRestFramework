from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.api.serializers import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)