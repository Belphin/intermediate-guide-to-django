from rest_framework import serializers
from django.core.paginator import Paginator
from .models import Board, Topic


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class BoardsTableSerializer(serializers.Serializer):
    items = serializers.SerializerMethodField()
    total_elements = serializers.SerializerMethodField()
    total_pages = serializers.SerializerMethodField()

    def get_items(self, options):
        queryset = Board.objects.all()
        paginator = Paginator(queryset, options['limit'])
        items = paginator.page(options['page'])
        return BoardSerializer(items, many=True).data

    def get_total_elements(self, options):
        queryset = Board.objects.all()
        paginator = Paginator(queryset, options['limit'])
        return paginator.count

    def get_total_pages(self, options):
        queryset = Board.objects.all()
        paginator = Paginator(queryset, options['limit'])
        return paginator.num_pages


class TopicTableSerializer(serializers.Serializer):
    topics = serializers.SerializerMethodField()
    total_topics = serializers.SerializerMethodField()
    total_topics_pages = serializers.SerializerMethodField()

    def get_topics(self, options):
        board = Board.objects.filter(pk=options["board_id"]).first()
        data = BoardSerializer(board).data

        topics = Topic.objects.filter(board__name=board.name)

        paginator = Paginator(topics, options['limit'])
        topics = paginator.page(options['page'])

        data["topics"] = TopicSerializer(topics, many=True).data
        return data

    def get_total_topics(self, options):
        board = Board.objects.filter(pk=options["board_id"]).first()
        topics = Topic.objects.filter(board__name=board.name)
        return topics.count()

    def get_total_topics_pages(self, options):
        board = Board.objects.filter(pk=options["board_id"]).first()
        topics = Topic.objects.filter(board__name=board.name)
        paginator = Paginator(topics, options['limit'])
        return paginator.num_pages