from django.db import models


# Create your models here.

sex = (
        ('H', 'Hombre'), 
        ('M', 'Mujer')
        )

class Sexo(models.Model):

    sexo = models.CharField(max_length=40,choices= sex)


class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()


    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// COMISION: {self.comision}" )
    


class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=150)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=40)

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// Apellidos: {self.apellidos}" )
    

""" class Maestro(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=2, choices=Sexo, blank=False, default='H')
    titulo = models.CharField(max_length=12, blank=False, default='Lic')


    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// Apellidos: {self.apellidos} /// Titulo:{self.titulo}" ) """
