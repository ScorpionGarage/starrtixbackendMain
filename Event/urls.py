from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ticketViewSet,BookingViewset

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tickets', ticketViewSet)
router.register(r'booking',BookingViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('booking/create/', BookingViewset.as_view({'post': 'create'}))
]
