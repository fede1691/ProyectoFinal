from django.urls import path
from AppPagina import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('saludo', views.saludo, name="Saludo"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('alumnoFormulario', views.alumnoFormulario, name="AlumnoFormulario"),
    path('maestroFormulario', views.maestroFormulario, name="MaestroFormulario"),
    path('leerCursos', views.leerCursos, name="LeerCursos"),
    path('eliminarCursos/<curso_nombre>', views.eliminarCursos, name="EliminarCursos"),
    path('editarCursos/<curso_nombre>', views.editarCursos, name="EditarCursos"),
    path('curso/lista', views.ListaCursos.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$', views.DetalleCursos.as_view(), name="Detail"),
    path(r'^nuevo$', views.CreacionCursos.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.ActualizaCursos.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.BorrarCursos.as_view(), name="Delete"),
    path('alumno/lista', views.ListaAlumno.as_view(), name="ListAlumno"),
    path(r'^detalleAlumno/(?P<pk>\d+)$', views.DetalleAlumno.as_view(), name="DetailAlumno"),
    path(r'^nuevoAlumno$', views.NuevoAlumno.as_view(), name="NewAlumno"),
    path(r'^editarAlumno/(?P<pk>\d+)$', views.ActualizaAlumno.as_view(), name="EditAlumno"),
    path(r'^borrarAlumno/(?P<pk>\d+)$', views.BorrarAlumno.as_view(), name="DeleteAlumno"),
    
]