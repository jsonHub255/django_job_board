from django.db import models

# Create your models here.
class Job(models.Model): # Create a table `Job`
    title = models.CharField(max_length=100) # Create table field `tile`
    