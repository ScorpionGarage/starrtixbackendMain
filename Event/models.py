from django.db import models
from django.conf import settings
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
import secrets
from django.contrib.staticfiles import finders
from PIL import Image

class Event(models.Model):
    title = models.CharField(max_length=255)
    types=models.CharField(max_length=255)
    event=models.TimeField()
    eventstarttime= models.TimeField()
    eventendtime=models.TimeField()
    eventtags=models.CharField()
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/', default="freepic.com")
    video = models.FileField(upload_to='videos/', default="freepic.com")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional price field

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
    
    
    # invitaion
class invitation(models.Model):
        nameofattendee = models.TextField()
        expirationdate= models.DateField()
        numberofinvitaion= models.IntegerField()
        uniqueIdentidier =  models.CharField(max_length=20, blank=True, null=True)
        email= models.EmailField()
        unique_id = models.CharField(max_length=4, editable=False, unique=True)  # Updated field type
        qrcode= models.ImageField(upload_to='qrcodes/', blank=True, null=True)
        event=models.ForeignKey(Event, on_delete=models.CASCADE)

        def save(self, *args, **kwargs):
           self.unique_id = secrets.token_urlsafe(3)[:4]  # Generate a new 4-character string

           qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
           )
           qr_data = f"{self.unique_id}"
           qr.add_data(qr_data)
           qr.make(fit=True)
 
           img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # Load the logo and calculate the positioning
           logo_path = finders.find('images/starrtix.png')  # Specify path to the logo image
           logo = Image.open(logo_path)
           logo_size = 30  # Adjust the size of the logo as needed
           logo = logo.resize((logo_size, logo_size))

        # Get dimensions to place the logo at the center
           qr_width, qr_height = img.size
           logo_width, logo_height = logo.size
           x = (qr_width - logo_width) // 2
           y = (qr_height - logo_height) // 2

        # Paste the logo onto the QR code
           img.paste(logo, (x, y), logo)  # The third parameter is for 'mask' which ensures transparency

        # Save the modified QR code with the logo
           fname = f'qrcode-{self.unique_id}.png'
           buffer = BytesIO()
           img.save(buffer, 'PNG')
           self.qrcode.save(fname, File(buffer), save=False)

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
        qr_data = f"{self.unique_id}"
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        fname = f'qrcode-{self.unique_id}.png'
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)

        super().save(*args, **kwargs)
    