from django.db import models
from django.conf import settings
import uuid
import qrcode
from io import BytesIO
from django.core.files import File

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
    def save(self, *args, **kwargs):
        self.ticketleft = self.ticketnumber- self.ticketsold
        super().save(*args, **kwargs)
    
    
    
    
# booking
class Booking(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email= models.EmailField()
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    booked_on= models.DateTimeField(auto_now_add=True)
    unique_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    qrcode= models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    number_of_tickets=models.PositiveIntegerField(default=1)  # this will be the number
    
    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f"Booking ID: {self.unique_id}\nName: {self.name}"
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        fname = f'qrcode-{self.unique_id}.png'
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)

        super().save(*args, **kwargs)
    