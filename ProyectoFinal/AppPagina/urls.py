from django.urls import path
from AppPagina import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('saludo', views.saludo, name="Saludo"),
    path('login', views.login_request, name="Login"),
    path('signup', views.signup, name="SignUp"),
    path('logout', LogoutView.as_view(template_name='AppPagina/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('about', views.about, name="About"),

    ## URLS BUSQUEDA ##

    ## ALUMNO ##
    path('busqueda_alumno', views.busquedaAlumno, name="BusquedaAlumno"),
    path('buscarAlumno/', views.buscarAlumno, name="BuscarAlumno"),

        
    ## MAESTRO ##    
    
    path('busqueda_maestro', views.busquedaMaestro, name="BusquedaMaestro"),
    path('buscarMaestro/', views.buscarMaestro, name="BuscarMaestro"),
    
    ## CURSOS ##
    path('busquedaCurso', views.busquedaCurso, name='BusquedaCurso'),
    path('buscarCurso/', views.buscarCurso, name='BuscarCurso'),
    ####################################################


    ## CURSOS ## 

    path('curso/lista', views.ListaCursos.as_view(), name="ListaCursos"),
    path(r'^(?P<pk>\d+)$', views.DetalleCursos.as_view(), name="DetalleCursos"),
    path(r'^nuevo$', views.CrearCurso.as_view(), name="CrearCurso"),
    path(r'^editar/(?P<pk>\d+)$', views.EditarCursos.as_view(), name="EditarCursos"),
    path(r'^borrar/(?P<pk>\d+)$', views.BorrarCursos.as_view(), name="BorrarCursos"),

    ## ALUMNOS ##
    
    path('alumno/lista', views.ListaAlumnos.as_view(), name="ListaAlumnos"),
    path(r'^detalleAlumno/(?P<pk>\d+)$', views.DetalleAlumno.as_view(), name="DetalleAlumno"),
    path(r'^nuevoAlumno$', views.CrearAlumno.as_view(), name="CrearAlumno"),
    path(r'^editarAlumno/(?P<pk>\d+)$', views.ActualizaAlumno.as_view(), name="EditarAlumno"),
    path(r'^borrarAlumno/(?P<pk>\d+)$', views.BorrarAlumno.as_view(), name="BorrarAlumno"),
    

    ## MAESTROS ##
    path('maestro/lista', views.ListaMaestro.as_view(), name="ListaMaestro"),
    path(r'^detalleMaestro/(?P<pk>\d+)$', views.DetalleMaestro.as_view(), name="DetalleMaestro"),
    path(r'^nuevoMaestro$', views.CrearMaestro.as_view(), name="CrearMaestro"),
    path(r'^editarMaestro/(?P<pk>\d+)$', views.EditarMaestro.as_view(), name="EditarMaestro"),
    path(r'^borrarMaestro/(?P<pk>\d+)$', views.BorrarMaestro.as_view(), name="BorrarMaestro"),
]