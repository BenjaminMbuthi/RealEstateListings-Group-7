from rest_framework import serializers
from .models import Agent, Location, Property, Buyer, Listing


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    location = LocationSerializer()  # Nested serializer for Location
    agent = AgentSerializer()  # Nested serializer for Agent

    class Meta:
        model = Property
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    property = PropertySerializer()  # Nested serializer for Property
    buyer = BuyerSerializer()  # Nested serializer for Buyer

    class Meta:
        model = Listing
        fields = '__all__'
