from django.shortcuts import render
from rest_framework import viewsets

from .models import Cancha, Reserva
from .serializers import CanchaSerializer, ReservaSerializer, UsuarioSerializer
from django.contrib.auth.models import User


class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def get_queryset(self):
        queryset = Reserva.objects.all()
        cancha = self.request.query_params.get('canchaId', None)
        print(cancha)
        if cancha is not None:
            queryset = queryset.filter(cancha=cancha)
        return queryset
        


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

