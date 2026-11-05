

from rest_framework import serializers

from reservation.models import Booking

class BookingSerializer(serializers.Serializer):


    id = serializers.CharField(read_only=True)

    name = serializers.CharField()

    phone = serializers.CharField()

    email = serializers.EmailField()

    turf = serializers.IntegerField()

    match_date = serializers.DateField()

    duration = serializers.IntegerField()

    start_time = serializers.TimeField()

    end_time = serializers.TimeField(read_only=True)

    amount = serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)


    def create(self, validated_data):

        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):

        for attribute,value in validated_data.items():

            setattr(instance,attribute,value)

        return instance













