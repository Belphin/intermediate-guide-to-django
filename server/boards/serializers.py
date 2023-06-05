from rest_framework import serializers
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


class BoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Topic
		fields = '__all__'


class BoardsTableSerializer(serializers.Serializer):
	data = serializers.SerializerMethodField()

	def get_data(self, options):

		queryset = Board.objects.all()
		paginator = Paginator(queryset, options['limit'])

		items = paginator.page(options['page'])
		total_elements = paginator.count
		total_pages = paginator.num_pages

		return {
			'items': BoardSerializer(items, many=True).data,
			'total_elements': total_elements,
			'total_pages': total_pages
		}


class TopicTableSerializer(serializers.Serializer):
	data = serializers.SerializerMethodField()

	def get_data(self, options):

		board = get_object_or_404(Board, pk=options["board_id"])
		data = BoardSerializer(board).data

		topics = Topic.objects.filter(board__name=board.name)

		paginator = Paginator(topics, options['limit'])
		topics = paginator.page(options['page'])

		total_topics = paginator.count
		total_topics_pages = paginator.num_pages

		data["topics"] = TopicSerializer(topics, many=True).data
		data["total_topics"] = total_topics
		data["total_topics_pages"] = total_topics_pages

		return data

