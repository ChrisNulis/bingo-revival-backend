from django.shortcuts import render
from rest_framework import generics
from .serializers import DogSerializer
from .models import Dog

class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all().order_by('id')
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all().order_by('id')
    serializer_class = DogSerializer
