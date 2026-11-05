from django.db import models

# Create your models here.
# booking[id,name,phone,email,turf,match_date,start_time,end_time,duration,amount]

class Booking(models.Model):

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    turf = models.PositiveIntegerField()

    match_date = models.DateField()

    duration = models.PositiveIntegerField()

    start_time = models.TimeField()

    end_time = models.TimeField(null=True)

    amount = models.DecimalField(max_digits=10,decimal_places=2,null=True)

