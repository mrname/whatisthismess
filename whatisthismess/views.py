import logging

from copy import deepcopy

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .crazy_sauce import CrazySauce
from .models import Quark
from .serializers import QuarkSerializer

logger = logging.getLogger(__name__)

# Make your happy little viewsets here
class QuarkViewSet(viewsets.ModelViewSet):
    queryset = Quark.objects.all()
    serializer_class = QuarkSerializer


class CrazySauceView(APIView):

    def post(self, request):
        sauce = CrazySauce()
        old_stuff = request.data
        new_stuff = sauce.make_sauce(deepcopy(old_stuff), 2)
        return Response({'old_sauce': old_stuff, 'new_sauce': new_stuff})
