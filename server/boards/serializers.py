from rest_framework import serializers
from django.core.paginator import Paginator

from .models import *


class BoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		fields = '__all__'


class BoardsTableSerializer(serializers.Serializer):
	items = serializers.SerializerMethodField()

	def get_items(self, data):
		
		queryset  = Board.objects.all()
		paginator = Paginator(queryset, data['limit'])

		items = paginator.page(data['page'])

		return BoardSerializer(items, many=True).data