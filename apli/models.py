from django.db import models
from uuid import uuid4


# criando os atributos do dados

class Empresas(models.Model):
    id_empresas = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    doc = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    active = models.CharField(max_length=10)
    site = models.CharField(max_length=255)
