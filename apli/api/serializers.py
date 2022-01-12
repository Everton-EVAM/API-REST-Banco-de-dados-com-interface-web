from rest_framework import serializers
from apli import models


class ApliSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresas
        fields = '__all__'
