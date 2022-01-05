from rest_framework import viewsets
from apli.api import serializers
from apli import models

class ApliViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.ApliSerializer
    queryset = models.objects.all()
