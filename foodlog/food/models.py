from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name

class Measure(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    label = models.CharField(max_length=100, null=True)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    fiber = models.IntegerField()

    def __str__(self):
        return self.label

