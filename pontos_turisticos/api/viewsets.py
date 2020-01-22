from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.api.serializers import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer