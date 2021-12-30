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

########################### FUNCIONES PARA BORRAR DATOS DE MODELS#############################################

def eliminarCursos(request, curso_nombre):
 
    curso = Curso.objects.get(nombre=curso_nombre) # Trae todos los cursos y todos sus objetos.   
    
    curso.delete() 
    
    cursos = Curso.objects.all()
   
    contexto = {"cursos":cursos}
    
    return render(request, "AppPagina/leerCursos", contexto)

########################### FUNCIONES PARA EDITAR DATOS DE MODELS#############################################

""" def editarCursos(request, curso_nombre):
 
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

    return render(request, "AppPagina/editarCursos", {"miFormulario":miFormulario, "curso_nombre":curso_nombre}) """

########## FUNCIONES DE BUSQUEDA ##################


def busquedaAlumno(request):

    return render (request, "AppPagina/busquedaAlumno.html")

def buscar(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre=nombre)
        error = ''
        return render(request, "AppPagina/resultadoBusquedaAlumnos.html", {"alumnos": alumnos, "nombre": nombre})
    
    else:

        error = "El alumno no se encuentra en la lista o no enviaste datos para buscar"    

    return render(request, "AppPagina/busquedaAlumno.html" ,{'error': error})



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
    
class NuevoMaestro(CreateView):
    model = Maestro
    success_url = "/AppPagina/maestro/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo', 'titulo']

class ActualizaMaestro(UpdateView):
    model = Maestro
    success_url = "/AppPagina/maestro/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo', 'titulo']
    
class BorrarMaestro(DeleteView):
    model = Maestro
    success_url = "/AppPagina/maestro/lista"