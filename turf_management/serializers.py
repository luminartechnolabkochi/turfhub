
from rest_framework import serializers
from turf_management.models import Turf
class TurfSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    location=serializers.CharField()

    address=serializers.CharField()

    description = serializers.CharField()

    opening_time = serializers.TimeField()

    closing_time = serializers.TimeField()

    day_price = serializers.DecimalField(max_digits=10,decimal_places=2)
    
    night_price = serializers.DecimalField(max_digits=10,decimal_places=2)

    facilities = serializers.CharField()

    def create(self, validated_data):

        return Turf.objects.create(**validated_data)

    def update(self, instance, validated_data):

        """
        validated_data={
            "id": 1,
            "name": "JSK",
            "location": "Thiroor , Thrissur, pottore",
            "address": "jsk , thiroor , thrissur",
            "description": "soil ground 360",
            "opening_time": "06:00:00",
            "closing_time": "23:45:00",
            "day_price": "750.00",
            "night_price": "1550.00",
            "facilities": "parking , rest room, ground boy support"
            }
        """


        for attribute,value in validated_data.items():

            setattr(instance,attribute,value)

        return instance
