from django.db import models

# Create your models here.
class EmpData(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField(max_length=25)

def __str__(self):
    return self.name