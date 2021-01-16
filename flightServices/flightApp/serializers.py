from rest_framework import serializers
import re

from flightApp.models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flightNumber(self, flightNumber):
        if re.match("^[a-zA-Z0-9]*$", flightNumber) is None:
            raise serializers.ValidationError("Invalid flight number.")
        return flightNumber


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
