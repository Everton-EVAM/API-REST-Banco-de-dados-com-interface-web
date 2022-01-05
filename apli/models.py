from django.db import models
from uuid import uuid4

class Empresas(models.Model):
    id_empresas = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    doc = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    active = models.CharField(max_length=10)
    site = models.CharField(max_length=255)

class clientes(models.Model):
    id_clientes = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    doc = models.IntegerField()
    about = models.CharField(max_length=255)
    active = models.CharField(max_length=10)
    site = models.CharField(max_length=255)

class ofertas(models.Model):
    id_ofertas = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_costumer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    de = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    initial_value = models.IntegerField()
    amount = models.IntegerField()
    amount_type = models.CharField(max_length=10)

class lances(models.Model):
    id_lancas = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_offer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    value = models.IntegerField()
    amount = models.IntegerField()
