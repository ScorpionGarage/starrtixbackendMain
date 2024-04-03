from django.db import models
from django.conf import settings


## blog model
class blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    
