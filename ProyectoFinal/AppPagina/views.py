from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

from AppPagina.forms import CursoFormulario, AlumnoFormulario, MaestroFormulario
from AppPagina.models import Curso, Alumno, Maestro
# Importamos la librerias para poder manejar las CBV
from django.views.generic import ListView
# Importamos la librerias para poder manejar las CBV
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ProyectoFinal.AppPagina.models import Avatar


def inicio(request):

    diccionario = {}
    cantidadDeAvatares = 0

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)

        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1

        diccionario["avatar"] = [cantidadDeAvatares-1].imagen.url

    return render(request, "AppPagina/inicio.html" diccionario)


def saludo(request):

    return render(request, "AppPagina/saludo.html")


########## FUNCIONES DE BUSQUEDA ##################

## ALUMNO ##

def busquedaAlumno(request):

    return render(request, "AppPagina/busqueda_alumno.html")


def buscarAlumno(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        error = ''
        return render(request, "AppPagina/resultado_busqueda_alumnos.html", {"alumnos": alumnos, "nombre": nombre})

    else:

        error = "El alumno no se encuentra en la lista o no enviaste datos para buscar"

    return render(request, "AppPagina/busqueda_alumno.html", {'error': error})

## CURSO ##


def busquedaCurso(request):

    return render(request, "AppPagina/busqueda_curso.html")


def buscarCurso(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        error = ''
        return render(request, "AppPagina/resultado_busqueda_cursos.html", {"cursos": cursos, "nombre": nombre})

    else:

        error = "El curso no se encuentra en la lista o no enviaste datos para buscar"

    return render(request, "AppPagina/busqueda_curso.html", {'error': error})

## MAESTRO ##


def busquedaMaestro(request):

    return render(request, "AppPagina/busqueda_maestro.html")


def buscarMaestro(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        maestros = Maestro.objects.filter(nombre__icontains=nombre)
        error = ''
        return render(request, "AppPagina/resultado_busqueda_maestros.html", {"cursos": maestros, "nombre": nombre})

    else:

        error = "El maestro no se encuentra en la lista o no enviaste datos para buscar"

    return render(request, "AppPagina/busqueda_maestro.html", {'error': error})


######################## CLASES BASADAS EN VISTAS ---CBV---  ############################################################

######################## CBVs CURSO ##################################

class ListaCursos(ListView):
    model = Curso
    template_name = "AppPagina/lista_cursos"


class DetalleCursos(DetailView):
    model = Curso
    template_name = "AppPagina/detalle_cursos"


class CrearCurso(CreateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']


class EditarCursos(UpdateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']


class BorrarCursos(DeleteView):
    model = Curso
    success_url = "/AppPagina/curso/lista"

######################## CBVs ALUMNO ##################################


class ListaAlumnos(ListView):
    model = Alumno
    template_name = "AppPagina/lista_alumnos"


class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "AppPagina/alumno_detalle"


class CrearAlumno(CreateView):
    model = Alumno
    success_url = "/AppPagina/alumno/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo']


class ActualizaAlumno(UpdateView):
    model = Alumno
    success_url = "/AppPagina/alumno/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo']


class BorrarAlumno(DeleteView):
    model = Alumno
    success_url = "/AppPagina/alumno/lista"

######################## CBVs MAESTRO ##################################


class ListaMaestro(ListView):
    model = Maestro
    template_name = "AppPagina/maestro_list"


class DetalleMaestro(DetailView):
    model = Maestro
    template_name = "AppPagina/maestro_detalle"


class CrearMaestro(CreateView):
    model = Maestro
    success_url = "/AppPagina/maestro/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo', 'titulo']


class EditarMaestro(UpdateView):
    model = Maestro
    success_url = "/AppPagina/maestro/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo', 'titulo']


class BorrarMaestro(DeleteView):
    model = Maestro
    success_url = "/AppPagina/maestro/lista"
