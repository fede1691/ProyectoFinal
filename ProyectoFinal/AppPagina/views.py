from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

from AppPagina.forms import CursoFormulario, AlumnoFormulario, MaestroFormulario
from AppPagina.models import Curso, Alumno, Maestro
from django.views.generic import ListView # Importamos la librerias para poder manejar las CBV
from django.views.generic.detail import DetailView  # Importamos la librerias para poder manejar las CBV
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

            return render(request, "AppPagina/cursoFormulario")
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

########################### FUNCIONES PARA LEER MODELS#############################################

def leerCursos(request):
 
    cursos = Curso.objects.all() # Trae todos los cursos y todos sus objetos.   
 
    contexto = {"cursos":cursos}
    
    return render(request, "AppPagina/leerCursos", contexto)

########################### FUNCIONES PARA BORRAR DATOS DE MODELS#############################################

def eliminarCursos(request, curso_nombre):
 
    curso = Curso.objects.get(nombre=curso_nombre) # Trae todos los cursos y todos sus objetos.   
    
    curso.delete() 
    
    cursos = Curso.objects.all()
   
    contexto = {"cursos":cursos}
    
    return render(request, "AppPagina/leerCursos", contexto)

########################### FUNCIONES PARA EDITAR DATOS DE MODELS#############################################

def editarCursos(request, curso_nombre):
 
    curso = Curso.objects.get(nombre=curso_nombre) # Trae todos los cursos y todos sus objetos.   
    
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso.nombre = informacion['nombre'], 
            curso.comision = informacion['comision']

            curso.save()

            return render(request, "AppPagina/inicio.html")
    else:

        miFormulario = CursoFormulario(initial={'nombre':curso.nombre, 'comision':curso.comision})

    return render(request, "AppPagina/editarCursos", {"miFormulario":miFormulario, "curso_nombre":curso_nombre})

######################## CLASES BASADAS EN VISTAS ---CBV---  ############################################################

######################## CBVs CURSO ##################################
class ListaCursos(ListView):
    model = Curso
    template_name = "AppPagina/curso_list"

class DetalleCursos(DetailView):
    model = Curso
    template_name = "AppPagina/curso_detalle"
    
class CreacionCursos(CreateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']

class ActualizaCursos(UpdateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']
    
class BorrarCursos(DeleteView):
    model = Curso
    success_url = "/AppPagina/curso/lista"

######################## CBVs ALUMNO ##################################
class ListaAlumno(ListView):
    model = Alumno
    template_name = "AppPagina/alumno_list"

class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "AppPagina/alumno_detalle"
    
class NuevoAlumno(CreateView):
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