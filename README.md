# Proyecto CODER Curso PHP Django

_Este es un proyecto acad茅mico del curso Coder PHP Django, incluye todas las funcionalidades y/o funciones vistas en el mismo_

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._



## Pre-requisitos 馃搵

_Librerias o paquetes necesarios:_

```
asgiref==3.4.1
Django==4.0
sqlparse==0.4.2
tzdata==2021.5
```

## Instalaci贸n 馃敡

_1. Clona el repo utilizando git:_



```
git clone <url del repositorio>

```
_2. Inicia el servidor django_

```
python manage.py runserver <port>

```

## Ejecutando las pruebas 鈿欙笍

_Las funciones del aplicativo son:_
#### 1) Herencia de Templates
#### 2) Modelos
#### 3) Formulario


### 1) Herencia de Templates - Validaci贸n 馃敥

_Para validar que se simplific贸 el c贸digo html se implement贸 "Herencia de Templates", para verificar lo anterior realiza las siguientes tareas:_

_Tarea 1. Validar pagina de inicio de la APP: Se debe desplegar la p谩gina de inicio de la aplicaion mostrando un mensaje de BIENVENIDOS Aprendiendo Django_


```
Ingresar a: http://127.0.0.1:8000/AppPagina/
```
_Tarea 2. Validar herencia 1: Buscar el menu SALUDO y dar clic, debera cambiar la p谩gina y mostrar un nuevo mensaje_


```
http://127.0.0.1:8000/AppPagina/saludo
```
_Tarea 3. Validar herencia 2: Buscar el menu REGISTRO CURSO y dar clic, debera cambiar la p谩gina y mostrar un formulario_


```
http://127.0.0.1:8000/AppPagina/cursoFormulario
```

### 2) Modelos - Validaci贸n 鈱笍

_Tarea 1. Ingresar models.py: Para validar los modelos de datos de la APP ingresa al siguiente PATH_

```
ProyectoFinal/AppPagina/models.py
```

_Tarea 2. Validar models.py: Observa que existen al menos 3 modelos distintos de datos_

```
from django.db import models


# Create your models here.

sex = (
        ('H', 'Hombre'), 
        ('M', 'Mujer')
        )

tit = (
        ('Lic', 'Licenciatura'), 
        ('Mae', 'Maestr铆a'),
        ('Doc', 'Doctorado'),
        )

class Sexo(models.Model):

    sexo = models.CharField(max_length=40,choices= sex)
    
class Titulo(models.Model):

    titulo = models.CharField(max_length=40,choices= tit)


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
    

class Maestro(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)


    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// Apellidos: {self.apellidos} /// Titulo:{self.titulo}" )
```
### 3) Formulario - Validaci贸n 鈱笍

_Tarea 1. Ingresar al formulario: Accede al recurso formulario ubicando del menu REGISTRO CURSO dentro del NAV_

```
http://127.0.0.1:8000/AppPagina/cursoFormulario
```

_Tarea 2. Validar formulario: Ingresa los datos solicitados del formulario_

```
from django import forms
from AppPagina.models import sex, tit

YEARS= [x for x in range(1910,2021)]

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=YEARS))       
    sexo = forms.ChoiceField(choices=sex)
    
class MaestroFormulario(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=YEARS))       
    sexo = forms.ChoiceField(choices=sex)
    titulo = forms.ChoiceField(choices=tit)
```

## Construido con 馃洜锔?

_El proyecto se ha realizado utilizando:_

* [Python](https://www.python.org/downloads/) - Lenguaje de programaci贸n :snake:
* [Django](https://maven.apache.org/) - Frame de desarrollo :clapper:

## Autores 鉁掞笍

_Aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Federico G贸mez Catuogno** - *C贸digo: CSS, Menu, Login, M贸dulo Alumnos* - [Fede](https://github.com/fede1691)
* **Diego Nicolas Dasanbiagio** - *C贸digo: CSS, Menu, Logout, M贸ludo Cursos* - [Nico](https://github.com/)
* **Eliud Bueno Moreno** - *C贸digo:CSS, Menu, SignUp, M贸ldulo Maestros* - [xe2mbe](https://github.com/xe2mbe)
 

## Licencia 馃搫

Este proyecto no implica licencia alguna

## Expresiones de Gratitud 馃巵

* Gracias al instructor Nico Perez de Coder y a nuestra tutora Cintiha Pardos 馃摙




---
Team 4
