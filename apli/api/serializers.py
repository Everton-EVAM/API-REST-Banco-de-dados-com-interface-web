from rest_framework import serializers
from apli.models import models

class ApliSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.apli
        fields = '__all__'
