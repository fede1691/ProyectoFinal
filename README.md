# Proyecto CODER Curso PHP Django

_Este es un proyecto académico del curso Coder PHP Django, incluye todas las funcionalidades y/o funciones vistas en el mismo_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._



## Pre-requisitos 📋

_Librerias o paquetes necesarios:_

```
asgiref==3.4.1
Django==4.0
sqlparse==0.4.2
tzdata==2021.5
```

## Instalación 🔧

_1. Clona el repo utilizando git:_



```
git clone <url del repositorio>

```
_2. Inicia el servidor django_

```
python manage.py runserver <port>

```

## Ejecutando las pruebas ⚙️

_Las funciones del aplicativo son:_
#### 1) Herencia de Templates
#### 2) Modelos
#### 3) Formulario


### 1) Herencia de Templates - Validación 🔩

_Para validar que se simplificó el código html se implementó "Herencia de Templates", para verificar lo anterior realiza las siguientes tareas:_

_Tarea 1. Validar pagina de inicio de la APP: Se debe desplegar la página de inicio de la aplicaion mostrando un mensaje de BIENVENIDOS Aprendiendo Django_


```
Ingresar a: http://127.0.0.1:8000/AppPagina/
```
_Tarea 2. Validar herencia 1: Buscar el menu SALUDO y dar clic, debera cambiar la página y mostrar un nuevo mensaje_


```
http://127.0.0.1:8000/AppPagina/saludo
```
_Tarea 3. Validar herencia 2: Buscar el menu REGISTRO CURSO y dar clic, debera cambiar la página y mostrar un formulario_


```
http://127.0.0.1:8000/AppPagina/cursoFormulario
```

### 2) Modelos - Validación ⌨️

_Tarea 1. Ingresar models.py: Para validar los modelos de datos de la APP ingresa al siguiente PATH_

```
ProyectoFinal/AppPagina/models.py
```

_Tarea 2. Validar models.py: Observa que existen al menos 3 modelos distintos de datos_

```
class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()


    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// COMISION: {self.comision}" )
```
### 3) Formulario - Validación ⌨️

_Tarea 1. Ingresar al formulario: Accede al recurso formulario ubicando del menu REGISTRO CURSO dentro del NAV_

```
http://127.0.0.1:8000/AppPagina/cursoFormulario
```

_Tarea 2. Validar formulario: Ingresa los datos solicitados del formulario_

```
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
```

## Construido con 🛠️

_El proyecto se ha realizado utilizando:_

* [Python](https://www.python.org/downloads/) - Lenguaje de programación :snake:
* [Django](https://maven.apache.org/) - Frame de desarrollo :clapper:

## Autores ✒️

_Aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Fede** - *Código* - [Fede](https://github.com/fede1691)
* **Nico** - *Código* - [Nico](https://github.com/)
* **Eliud Bueno Moreno** - *Código* - [xe2mbe](https://github.com/xe2mbe)
 

## Licencia 📄

Este proyecto no implica licencia alguna

## Expresiones de Gratitud 🎁

* Gracias al instructor Nico Perez de Coder y a nuestra tutora Cintiha Pardos 📢




---
Team 4
