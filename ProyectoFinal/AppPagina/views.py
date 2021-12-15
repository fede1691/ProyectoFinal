from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

from AppPagina.forms import CursoFormulario, AlumnoFormulario, MaestroFormulario
from AppPagina.models import Curso, Alumno, Maestro

def inicio(request):

    return render(request, "AppPagina/inicio.html")


def saludo(request):

    return render(request, "AppPagina/saludo.html")

def cursoFormulario(request):
    
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre = informacion['nombre'], comision = informacion['comision'])

            curso.save()

            return render(request, "AppPagina/inicio.html")
    else:

        miFormulario = CursoFormulario()

    return render(request, "AppPagina/cursoFormulario", {"miFormulario":miFormulario})

def alumnoFormulario(request):
    
    if request.method == 'POST':

        formAlumno = AlumnoFormulario(request.POST)

        if formAlumno.is_valid():

            informacion = formAlumno.cleaned_data

            alumno = Alumno(nombre = informacion['nombre'], 
                            apellidos = informacion['apellidos'], 
                            nacimiento = informacion['nacimiento'], 
                            sexo = informacion['sexo'])

            alumno.save()

            return render(request, "AppPagina/inicio.html")
    else:

        formAlumno = AlumnoFormulario()

    return render(request, "AppPagina/alumnoFormulario", {"formAlumno":formAlumno})

def maestroFormulario(request):
    
    if request.method == 'POST':

        formMaestro = MaestroFormulario(request.POST)

        if formMaestro.is_valid():

            informacion = formMaestro.cleaned_data

            maestro = Maestro(nombre = informacion['nombre'], 
                              apellidos = informacion['apellidos'], 
                              nacimiento = informacion['nacimiento'], 
                              sexo = informacion['sexo'],
                              titulo = informacion['titulo'])

            maestro.save()

            return render(request, "AppPagina/inicio.html")
    else:

        formMaestro = MaestroFormulario()

    return render(request, "AppPagina/maestroFormulario", {"formMaestro":formMaestro})
