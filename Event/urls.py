from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ticketViewSet,BookingViewset,InvitationViewset

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'tickets', ticketViewSet)
router.register(r'booking',BookingViewset)
router.register(r'invitations', InvitationViewset, basename='invitation')
urlpatterns = [
    path('', include(router.urls)),
    path('booking/create/', BookingViewset.as_view({'post': 'create'})),
    path('events/<int:event_id>/invitations/', InvitationViewset.as_view({'get': 'list'}), name='invitation-list'),
    path('invitation/<uuid:unique_id>/', InvitationViewset.as_view({'get': 'retrieve_by_unique_id'}), name='invitation-retrieve-by-unique-id'),
]
