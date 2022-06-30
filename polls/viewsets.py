from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewset):
  queryset = models.Employee.object.all()
  serializer_class = serializers.EmployeeSerializers