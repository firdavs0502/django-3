from django.db import models

# Create your models here.


class Mashina(models.Model):
    nomi = models.CharField(max_length=20)
    narxi = models.IntegerField(default=1)
    rangi = models.CharField(max_length=20)
    yili = models.IntegerField(default=2000)


    def __str__(self):
        return self.nomi