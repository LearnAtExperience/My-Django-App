from django.db import models

# Create your models here.

class Employee(models.Model):
  fullname = models.CharField(max_length=50)
  emp_id = models.CharField(max_length=6)
  mobile = models.CharField(max_length=11)

