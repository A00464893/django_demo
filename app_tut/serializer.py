from rest_framework import serializers
from .models import Hotel

class Hotel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        # fields = ['id', 'hotel_name', 'hotel_price']
        fields = "__all__"
