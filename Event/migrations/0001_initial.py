# Generated by Django 4.2 on 2024-04-20 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=255)),
                ('event', models.TimeField()),
                ('eventstarttime', models.TimeField()),
                ('eventendtime', models.TimeField()),
                ('eventtags', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(default='freepic.com', upload_to='images/')),
                ('video', models.FileField(default='freepic.com', upload_to='videos/')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketnumber', models.IntegerField()),
                ('expirationdate', models.DateField()),
                ('ticketsold', models.IntegerField()),
                ('ticketleft', models.IntegerField()),
                ('ticketscanned', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
            ],
        ),
        migrations.CreateModel(
            name='invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofattendee', models.TextField()),
                ('expirationdate', models.DateField()),
                ('numberofinvitaion', models.IntegerField()),
                ('uniqueIdentidier', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('unique_id', models.CharField(editable=False, max_length=4, unique=True)),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(blank=True, max_length=20, null=True)),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
                ('number_of_tickets', models.PositiveIntegerField(default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
            ],
        ),
    ]
