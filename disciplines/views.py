from rest_framework import viewsets
from .models import Discipline
from .serializers import DisciplinesListSerializer


class DisciplinesViewSet(viewsets.ModelViewSet):
    """Листинг дисциплин"""
    serializer_class = DisciplinesListSerializer
    queryset = Discipline.objects.all()
