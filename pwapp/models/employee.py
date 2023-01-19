from pwapp.models import Person
from django.db import models

class Employee(Person):    

    RECIDENCE = [
        ('Interno','Interno'),
        ('Externo','Externo')
    ]

    area = models.CharField(max_length=250)
    recidence = models.CharField(max_length= 50, choices=RECIDENCE,)

    class Meta(Person.Meta):
        db_table = 'employe'

    def __str__(self):
        return self.name