from django.db import models
from django.contrib.auth.models import User


class Cancha(models.Model):
    nombre_cancha = models.CharField(max_length=50, unique=True, blank=False)
    codigo_interno = models.CharField(max_length=30, unique=True, blank=False)
    tipo_cancha = models.CharField(max_length=20, blank=False)
    vestuario_disponible = models.CharField(max_length=2, blank=False)
    iluminacion = models.CharField(max_length=2, blank=False)
    cesped_sintetico = models.CharField(max_length=2, blank=False)

    class Meta:
        ordering = ('nombre_cancha',)

    def __str__(self):
        return self.nombre_cancha + ', ' + self.tipo_cancha


class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=80, blank=False)
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    turno_reserva = models.DateTimeField(unique=True, blank=False)
    reserva_creada = models.DateTimeField(auto_now_add=True)
    

    class Meta():
        ordering = ('turno_reserva',)

    def __str__(self):
        return self.turno + self.cliente

