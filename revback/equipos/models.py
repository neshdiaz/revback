from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre
