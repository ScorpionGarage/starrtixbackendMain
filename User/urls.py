from django.urls import path
from .views import RegisterView, LoginView,UserDetailView,UserViewSet
from rest_framework.authtoken.views import obtain_auth_token  # If you still want to use the built-in view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='profile'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users'),
    # Optionally keep the built-in token auth endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
]
