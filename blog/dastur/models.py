from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    kasb = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    sana = models.DateField()
    mavzu = models.CharField(max_length=100)
    matn = models.CharField(max_length=300)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

