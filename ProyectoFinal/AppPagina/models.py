from django.db import models
from django.contrib.auth.models import User


# Create your models here.

sex = (
    ('H', 'Hombre'),
    ('M', 'Mujer')
)

tit = (
    ('Lic', 'Licenciatura'),
    ('Mae', 'Maestría'),
    ('Doc', 'Doctorado'),
)


class Sexo(models.Model):

    sexo = models.CharField(max_length=40, choices=sex)


class Titulo(models.Model):

    titulo = models.CharField(max_length=40, choices=tit)


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self) -> str:
        return (f"Nombre del Curso: {self.nombre} Comision: {self.comision}")


class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=150)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=40)

    def __str__(self) -> str:
        return (f"Nombre del Alumno: {self.nombre} Apellidos: {self.apellidos} Fecha Nacimiento: {self.nacimiento} Sexo: {self.sexo}")


class Maestro(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// Apellidos: {self.apellidos} /// Nacimiento: {self.nacimiento} Sexo: {self.sexo} /// Titulo:{self.titulo}")


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
