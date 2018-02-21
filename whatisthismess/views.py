import logging

from rest_framework import viewsets

from .models import Quark
from .serializers import QuarkSerializer

logger = logging.getLogger(__name__)

# Make your happy little viewsets here
class QuarkViewSet(viewsets.ModelViewSet):
    queryset = Quark.objects.all()
    serializer_class = QuarkSerializer
