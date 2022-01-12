from rest_framework import viewsets
from apli.api import serializers
from apli import models


class ApliViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ApliSerializer
    queryset = models.Empresas.objects.all()
