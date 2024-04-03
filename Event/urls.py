from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ticketViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tickets', ticketViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
