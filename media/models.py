from django.db import models
from django.conf import settings

# Create your models here.
# PROFILE PIC MODELS FOR USERS
class profilePicture(models.Model):
        image=models.ImageField(upload_to='images/')
        User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        
        
# Event PIC MODELS FOR USERS
class eventMedia(models.Model):
        image=models.ImageField(upload_to='images/')
        video = models.FileField(upload_to='videos/')
        event= models.ForeignKey('Event.Event',on_delete=models.CASCADE)
        

# Event PIC MODELS FOR USERS
class blogMedia(models.Model):
        image=models.ImageField(upload_to='images/')
        video = models.FileField(upload_to='videos/')
        blog = models.ForeignKey('blog.blog',on_delete=models.CASCADE)



