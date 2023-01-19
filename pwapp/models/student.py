from pwapp.models import Person
from django.db import models

class Student(Person):
    CAREERS = [
        ('Ingeniería en Ciencias Informáticas', 'Ingeniería en Ciencias Informáticas'),
        ('Ingeniería en Bioinformática', 'Ingeniería en Bioinformática'),
        ('Ingeniería en Ciberseguridad', 'Ingeniería en Ciberseguridad'),
        ('Administración de Redes y Seguridad Informática', 'Administración de Redes y Seguridad Informática'),
    ]
    ANNO = [
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
        ('Cuarto', 'Cuarto'),
        ('Quinto', 'Quinto'),
    ]

    careers = models.CharField(max_length=255, choices=CAREERS,)
    anno = models.CharField(max_length=255,choices=ANNO,)
    group = models.CharField(max_length=4)

    class Meta(Person.Meta):
        db_table = 'student'

    def __str__(self):
        return self.name