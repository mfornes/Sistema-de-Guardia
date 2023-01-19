from django.db import models

class Person(models.Model):
    SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),     
    ]
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO,)

    class Meta:
        abstract = True
        ordering = ['id']