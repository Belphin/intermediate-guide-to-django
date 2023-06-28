from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Board
from .serializers import *
from accounts.constants import UserRoleChoice

class BloggerOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoleChoice.BLOGGER


class BoardViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = BoardsPageSerializer(request.GET)
        return Response(serializer.data)


class TopicViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = TopicPageSerializer(request.GET)
        return Response(serializer.data)

    def create(self, request):
        serializer = TopicCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            topic = serializer.save()
            return Response(data=topic, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [BloggerOnlyPermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]