from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"boards-table", BoardViewSet, basename="home")
router.register(r"topics-table", TopicViewSet, basename="board_topics")

urlpatterns = [
    path("", include(router.urls))
]