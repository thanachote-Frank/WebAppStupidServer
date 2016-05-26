from django.db import models

# Create your models here.
class Job(models.Model):
    input = models.CharField(max_length=200)
    result = models.CharField(max_length=2000, null=True)
