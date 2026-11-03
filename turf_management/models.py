

# Create your models here.
from django.db import models


class Turf(models.Model):

    name = models.CharField(max_length=150)

    location = models.CharField(max_length=200)

    address = models.TextField()

    description = models.TextField()   

    opening_time = models.TimeField()

    closing_time = models.TimeField()

    day_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    night_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    facilities = models.TextField(
        blank=True,
        null=True
    )
   
    