from .models import *
from rest_framework import serializers
from django.db.models import Q,Count
from django.db.models.functions import TruncDate

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = "__all__"

from rest_framework import serializers

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()