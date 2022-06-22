from rest_framework import viewsets
from .import models
from .import serializers

class EmpViewset(viewsets.ModelViewSet):
    queryset=models.EmpData.objects.all()
    serializer_class=serializers.EmpDataSerializer
    