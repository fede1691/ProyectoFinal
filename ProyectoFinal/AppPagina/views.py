from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context, loader

from AppPagina.forms import CursoFormulario, AlumnoFormulario, MaestroFormulario, RegistroFormulario, UserEditForm
from AppPagina.models import Curso, Alumno, Maestro
from django.views.generic import ListView # Importamos la librerias para poder manejar las CBV
from django.views.generic.detail import DetailView  # Importamos la librerias para poder manejar las CBV
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import login,logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def inicio(request):

    return render(request, "AppPagina/inicio.html")

def saludo(request):

    return render(request, "AppPagina/saludo.html")


def about(request):

    return render(request, "AppPagina/about.html")

def cursoFormulario(request):
    
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render(request, "/AppPagina/inicio.html", {"mensaje": "Usuario Creado"})

    else:

        form = UserCreationForm()

    return render(request, "/AppPagina/inicio.html", {"form": form})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)

                return render(request,"AppPagina/inicio.html", {"mensaje" : f"Bienvenido/a {usuario} "})

            else:

                return render(request,"AppPagina/inicio.html", {"mensaje" : "Error datos incorrectos "})

        else:

                return render(request,"AppPagina/inicio.html", {"mensaje" : "Error formulario erroneo "})

    form = AuthenticationForm()

    return render(request, "AppPagina/login.html", {"form": form})



########## FUNCIONES DE BUSQUEDA ##################

## ALUMNO ##

def busquedaAlumno(request):

    return render (request, "AppPagina/busqueda_alumno.html")

def buscarAlumno(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        error = ''
        return render(request, "AppPagina/resultado_busqueda_alumnos.html", {"alumnos": alumnos, "nombre": nombre})
########################### FUNCIONES PARA BORRAR DATOS DE MODELS#############################################

## CURSO ##

def busquedaCurso(request):

    return render (request, "AppPagina/busquedaCurso.html")

def buscarCurso(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        error = ''
        return render(request, "AppPagina/resultado_busqueda_cursos.html", {"cursos": cursos, "nombre": nombre})
    
    else:

        error = "El curso no se encuentra en la lista o no enviaste datos para buscar"    

    return render(request, "AppPagina/busquedaCurso.html" ,{'error': error})

## MAESTRO ##

def busquedaMaestro(request):

    return render (request, "AppPagina/busqueda_maestro.html")

def buscarMaestro(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        maestros = Maestro.objects.filter(nombre__icontains= nombre)
        error = ''
        return render(request, "AppPagina/resultado_busqueda_maestros.html", {"cursos": maestros, "nombre": nombre})
    
    else:

        error = "El maestro no se encuentra en la lista o no enviaste datos para buscar"    

    return render(request, "AppPagina/busqueda_maestro.html" ,{'error': error})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            return render(request, "AppPagina/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "AppPagina/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


######################## CLASES BASADAS EN VISTAS ---CBV---  ############################################################

######################## CBVs CURSO ##################################

class ListaCursos(LoginRequiredMixin,ListView):
    model = Curso
    template_name = "AppPagina/lista_cursos"

class DetalleCursos(LoginRequiredMixin,DetailView):
    model = Curso
    template_name = "AppPagina/detalle_cursos"
    
class CrearCurso(LoginRequiredMixin,CreateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']

class EditarCursos(LoginRequiredMixin,UpdateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']
    
class BorrarCursos (LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = "/AppPagina/curso/lista"

######################## CBVs ALUMNO ##################################
class ListaAlumnos(LoginRequiredMixin,ListView):
    model = Alumno
    template_name = "AppPagina/lista_alumnos"

class DetalleAlumno(LoginRequiredMixin,DetailView):
    model = Alumno
    template_name = "AppPagina/alumno_detalle"
    
class CrearAlumno(LoginRequiredMixin,CreateView):
    model = Alumno
    success_url = "/AppPagina/alumno/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo']

class ActualizaAlumno(LoginRequiredMixin,UpdateView):
    model = Alumno
    success_url = "/AppPagina/alumno/lista"
    fields = ['nombre', 'apellidos', 'nacimiento', 'sexo']
    
class BorrarAlumno(LoginRequiredMixin,DeleteView):
    model = Alumno
    success_url = "/AppPagina/alumno/lista"

######################## CBVs MAESTRO ##################################

class ListaMaestro(ListView):
    model = Maestro
    template_name = "AppPagina/maestro_list"

class DetalleMaestro(DetailView):
    model = Maestro
    template_name = "AppPagina/maestro_detalle"
    
class CrearMaestro(LoginRequiredMixin,CreateView):
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
    
    
############################ VISTA DE LOGIN#################################
#@csrf_exempt
def login_request(request):
    
    if request.method == "POST": # Verificamos si el method request is POST, si es TRUE hacemos....
        form= AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                return render(request, "AppPagina/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppPagina/inicio.html", {"mensaje": "datos incorrectos"})
        else:
            return render(request, "AppPagina/inicio.html", {"mensaje":"Error, verifica datos"})
        
        
    form = AuthenticationForm()  # Se genera un formulario vacio si se genera un POST vacio
    return render(request, "AppPagina/login.html", {'form':form})
        
        
############################ VISTA DE SIGN UP#################################
#@csrf_exempt
def signup(request):
    
    if request.method == "POST": # Verificamos si el method request is POST, si es TRUE hacemos....
        
        form= RegistroFormulario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppPagina/inicio.html", {"mensaje":f"{username} creado exitosamente"})
    
    else:
        form = RegistroFormulario()
    
        return render(request, "AppPagina/signup.html", {"form":form})

############################ VISTA DE LOGOUT#################################
#@csrf_exempt
def signup(request):
    
    if request.method == "POST": # Verificamos si el method request is POST, si es TRUE hacemos....
        
        form= RegistroFormulario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppPagina/inicio.html", {"mensaje":f"{username} creado exitosamente"})
    
    else:
        form = RegistroFormulario()
    
        return render(request, "AppPagina/signup.html", {"form":form})
