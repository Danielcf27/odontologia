from django.db import models
from django.db.models.base import Model

# Create your models here.
class Clientes(models.Model):
    Nombre= models.TextField(max_length=30)
    Apellido= models.TextField(max_length=30)
    Telefono= models.IntegerField() 
    Direccion= models.TextField(max_length=100)