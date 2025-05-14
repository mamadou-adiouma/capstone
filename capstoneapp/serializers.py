from rest_framework import serializers
from capstoneapp.models import Menu, Booking
from django.contrib.auth.models import User


# class userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         field = ["url", "username", "email", "groups"]


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
