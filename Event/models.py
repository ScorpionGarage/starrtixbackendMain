from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=255)
    types=models.CharField(max_length=255)
    event=models.TimeField()
    eventstarttime= models.TimeField()
    eventendtime=models.TimeField()
    eventtags=models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/', default="freepic.com")
    video = models.FileField(upload_to='videos/', default="freepic.com")
    def __str__(self):
        return self.title



## ticket model
class ticket(models.Model):
    ticketnumber = models.IntegerField()
    expirationdate= models.DateField()
    ticketsold = models.IntegerField()
    ticketleft= models.IntegerField()
    ticketscanned= models.IntegerField()
    event= models.ForeignKey('Event',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.ticketnumber
    
    