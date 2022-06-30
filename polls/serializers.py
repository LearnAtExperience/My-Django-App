from rest_framework import serializers

from .models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
  class Meta:
    model  =  Employee
    field = '__all__'
