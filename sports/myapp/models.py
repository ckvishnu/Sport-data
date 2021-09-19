from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    number_of_games=models.IntegerField()
    total_score=models.IntegerField()
    