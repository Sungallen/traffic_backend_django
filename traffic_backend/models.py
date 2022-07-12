from statistics import mode
from django.db import models

class flows(models.Model): 
    category = models.CharField(max_length=15)
    location = models.CharField(max_length=20)
    flow = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.category
