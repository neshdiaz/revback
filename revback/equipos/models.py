from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=64)
    
    # Foreign key
    lider = models.CharField(max_length=64)
    usuarios = models.CharField(max_length=64)

