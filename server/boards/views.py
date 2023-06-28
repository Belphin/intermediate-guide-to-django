from rest_framework import viewsets
from rest_framework.response import Response
from .models import Board
from .serializers import BoardsTableSerializer, TopicTableSerializer


class BoardViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        serializer = BoardsTableSerializer(data)
        return Response(serializer.data)


class TopicViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        serializer = TopicTableSerializer(data)
        return Response(serializer.data)