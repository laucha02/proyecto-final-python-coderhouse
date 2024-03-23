
from django.urls import path
from AppEntrega3Trueba.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio, name='Inicio'),
    path('jugadores/',jugadores, name='Jugadores'),
    path('estadios/',estadios,name='Estadios'),
    path('clubes/',clubes,name='Clubes'),
    #path('jugadoresFormulario/', jugadores_formulario, name="jugadoresFormulario"),
    #path('clubesFormulario/',clubes_formulario, name='clubesFormulario'),
    #path('estadiosFormulario/',estadios_formulario,name='estadiosFormulario'),
    path('buscarJugador/',buscar_jugador,name='buscarJugador'),
    path('buscandoJugador/',buscando_jugador),
    path('buscarClub/',buscar_club, name='buscarJugador'),
    path('buscandoClub/',buscando_club),
    path('buscarEstadio/',buscar_estadio,name='buscarEstadio'),
    path('buscandoEstadio/',buscando_estadio),

    path('leerJugadores/', leer_jugadores, name='leerJugadores'),
    path('eliminarJugador/<jugadorNombre>/',eliminar_jugadores, name="EliminarJugador"),
    path('editarJugadores/<jugadorNombre>/',editar_jugadores, name='EditarJugador'),


    path('club/list/', ListaClub.as_view(), name='LeerClubes'),
    path('club/<int:pk>/', DetalleClub.as_view(), name='DetalleClub'),
    path('club/crear/', CrearClub.as_view(),name='CrearClub'),
    path('club/editar/<int:pk>', ActualizarClub.as_view(),name='ActualizarClub'),
    path('club/borrar/<int:pk>', BorrarClub.as_view(),name='BorrarClub'),

    path('estadio/list/', ListaEstadio.as_view(), name='LeerEstadios'),
    path('estadio/<int:pk>/', DetalleEstadio.as_view(), name='DetalleEstadio'),
    path('estadio/crear/', CrearEstadio.as_view(),name='CrearEstadio'),
    path('estadio/editar/<int:pk>', ActualizarEstadio.as_view(),name='ActualizarEstadio'),
    path('estadio/borrar/<int:pk>', BorrarEstadio.as_view(),name='BorrarEstadio'),
    
    path('jugador/list/', ListaJugador.as_view(), name='LeerJugadores'),
    path('jugador/<int:pk>/', DetalleJugador.as_view(), name='DetalleJugador'),
    path('jugador/crear/', CrearJugador.as_view(),name='CrearJugador'),
    path('jugador/editar/<int:pk>', ActualizarJugador.as_view(),name='ActualizarJugador'),
    path('jugador/borrar/<int:pk>', BorrarJugador.as_view(),name='BorrarJugador'),


    path('login/', login_request, name ="Login"),
    path('registro/',registro, name='Register'),
    path('logout/',LogoutView.as_view(template_name ='AppEntrega3Trueba/logout.html'),name='Logout'),
    path('editar/', editar_usuario, name='EditarUsuario'),

    path('agregaravatar/',agregar_avatar,name='Avatar')

]