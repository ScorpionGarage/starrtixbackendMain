from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventMediaView, BlogMediaView, ProfilePicView
router = DefaultRouter()
router.register(r'event', EventMediaView)
router.register(r'blog', BlogMediaView)
router.register(r'profilepic', ProfilePicView)

urlpatterns = [
    path('', include(router.urls))
]
