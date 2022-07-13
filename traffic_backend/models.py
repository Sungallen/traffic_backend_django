from django.db import models


class category(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category

class coordinates(models.Model):
    coordinates = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=50)
    def __str__(self):
        return self.descriptions

class flows(models.Model): 
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    coordinates = models.ForeignKey(coordinates, on_delete=models.CASCADE)
    flow = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.category)

