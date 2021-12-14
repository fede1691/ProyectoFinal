from django.urls import path
from AppPagina import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('saludo', views.saludo, name="Saludo"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('alumnoFormulario', views.alumnoFormulario, name="AlumnoFormulario"),
]