# Generated by Django 4.2 on 2024-04-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]