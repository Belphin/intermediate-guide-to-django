from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Board
from .serializers import *
from .utils import set_default_keys


class BoardViewSet(viewsets.ModelViewSet):

	def create(self, request):
		data = request.data

		options = set_default_keys(data, {"page": "1", "limit": "10"})

		serializer = BoardsTableSerializer(options)
		return Response(serializer.data)


class TopicViewSet(viewsets.ModelViewSet):

	def create(self, request):
		data = request.data

		options = set_default_keys(data, {"board_id": "1", "page": "1", "limit": "10"})

		serializer = TopicTableSerializer(options)
		return Response(serializer.data)