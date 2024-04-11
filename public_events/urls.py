# public_events/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicEventViewSet

router = DefaultRouter()
router.register(r'events', PublicEventViewSet, basename='public-events')

urlpatterns = [
    path('', include(router.urls)),
]
