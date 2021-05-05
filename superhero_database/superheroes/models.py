from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=50)
    secret_identity = models.CharField(max_length=50)
    main_power = models.CharField(max_length=50)
    secondary_power = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name
