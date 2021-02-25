from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ticket_serializer
from .models import ticket

# Create your views here.

class ticket_view(viewsets.ModelViewSet):
    serializer_class = ticket_serializer
    queryset = ticket.objects.all()
