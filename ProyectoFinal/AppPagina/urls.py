from django.urls import path
from AppPagina import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('saludo', views.saludo, name="Saludo"),

    ##FORMULARIOS
    path('busquedaAlumno', views.busquedaAlumno, name="BusquedaAlumno"),
    path('buscar/', views.buscar, name="Buscar"),


    ##CURSOS
     
    path('curso/lista', views.ListaCursos.as_view(), name="ListaCursos"),
    path(r'^(?P<pk>\d+)$', views.DetalleCursos.as_view(), name="DetalleCursos"),
    path(r'^nuevo$', views.CrearCurso.as_view(), name="CrearCurso"),
    path(r'^editar/(?P<pk>\d+)$', views.EditarCursos.as_view(), name="EditarCursos"),
    path(r'^borrar/(?P<pk>\d+)$', views.BorrarCursos.as_view(), name="BorrarCursos"),

    ##ALUMNOS
    
    path('alumno/lista', views.ListaAlumnos.as_view(), name="ListaAlumnos"),
    path(r'^detalleAlumno/(?P<pk>\d+)$', views.DetalleAlumno.as_view(), name="DetalleAlumno"),
    path(r'^nuevoAlumno$', views.CrearAlumno.as_view(), name="CrearAlumno"),
    path(r'^editarAlumno/(?P<pk>\d+)$', views.ActualizaAlumno.as_view(), name="EditarAlumno"),
    path(r'^borrarAlumno/(?P<pk>\d+)$', views.BorrarAlumno.as_view(), name="BorrarAlumno"),
    

    ##MAESTROS
    
    path('maestro/lista', views.ListaMaestro.as_view(), name="ListMaestro"),
    path(r'^detalleMaestro/(?P<pk>\d+)$', views.DetalleMaestro.as_view(), name="DetailMaestro"),
    path(r'^nuevoMaestro$', views.NuevoMaestro.as_view(), name="NewMaestro"),
    path(r'^editarMaestro/(?P<pk>\d+)$', views.ActualizaMaestro.as_view(), name="EditMaestro"),
    path(r'^borrarMaestro/(?P<pk>\d+)$', views.BorrarMaestro.as_view(), name="DeleteMaestro"),
]