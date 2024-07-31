from django.db import models
from django.contrib.auth.models import User
from equipos.models import Equipo


class Usuario(models.Model):
    usuario_auth = models.OneToOneField(User, on_delete=models.CASCADE)
    en_equipos = models.ManyToManyField(Equipo, related_name="usuarios_del_equipo")
    lidera_equipos = models.ManyToManyField(Equipo, related_name="lideres")

    def __str__(self):
        return self.usuario_auth.first_name



class Permiso(models.Model):
    usuario = models.ManyToManyField(Usuario)
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre
