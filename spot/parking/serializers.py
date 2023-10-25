from rest_framework import serializers
from . import models

class ReservationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReservationInfo
        fields = \
            '__all__'

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParkingLot
        fields = \
            '__all__'

class ParkingZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParkingZone
        fields = \
            '__all__'

class ReservationStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReservationState
        fields = \
            '__all__'

class ParkingStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParkingState
        fields = \
            '__all__'