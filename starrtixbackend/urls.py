
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('User.urls')),
    path('event/', include('Event.urls')),
    path('pic/', include('media.urls')),
]
