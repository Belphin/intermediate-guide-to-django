from rest_framework import viewsets, status
from rest_framework.response import Response


class BoardViewSet(viewsets.ViewSet):

	def list(self, request):
		data = request.GET.dict()

		return Response(data)