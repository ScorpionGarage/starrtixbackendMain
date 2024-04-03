from django.contrib import admin
from .models import eventMedia, blogMedia, profilePicture


# Register your models here.
admin.site.register(eventMedia)
admin.site.register(blogMedia)
admin.register(profilePicture)