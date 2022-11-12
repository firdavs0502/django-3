from django.db import models

# Create your models here.


class Kofe(models.Model):
    nomi = models.CharField(max_length=20)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.nomi