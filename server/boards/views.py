from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Board
from .serializers import *


class BoardViewSet(viewsets.ViewSet):

	def list(self, request):
		data = request.GET.dict()
		serializer = BoardsTableSerializer(data)
		return Response(serializer.data)