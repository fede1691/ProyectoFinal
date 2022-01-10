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
from django.contrib.auth import login, logout, authenticate
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
@login_required
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
class ListaCursos(ListView):
    model = Curso
    template_name = "AppPagina/curso_list"

class DetalleCursos(DetailView):
    model = Curso
    template_name = "AppPagina/curso_detalle"
    
class CreacionCursos(LoginRequiredMixin,CreateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']

class ActualizaCursos(LoginRequiredMixin,UpdateView):
    model = Curso
    success_url = "/AppPagina/curso/lista"
    fields = ['nombre', 'comision']
    
class BorrarCursos (LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = "/AppPagina/curso/lista"

######################## CBVs ALUMNO ##################################
class ListaAlumno(ListView):
    model = Alumno
    template_name = "AppPagina/alumno_list"

class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "AppPagina/alumno_detalle"
    
class NuevoAlumno(LoginRequiredMixin,CreateView):
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