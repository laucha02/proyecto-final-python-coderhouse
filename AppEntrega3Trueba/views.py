from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega3Trueba.models import *
from AppEntrega3Trueba.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#from AppEntrega3Trueba.models import Curso

# Create your views here.


def login_request(request):

     if request.method == 'POST':

          form = AuthenticationForm(request, data = request.POST)

          if form.is_valid():

               usuario = form.cleaned_data.get('username')
               contraseña = form.cleaned_data.get('password')

               user = authenticate(username=usuario, password=contraseña)

               if user is not None:

                    login(request,user)

                    return render(request, 'AppEntrega3Trueba/inicio.html', {'mensaje':f'Bienvenido {user}'})
          else:

               return render(request, 'AppEntrega3Trueba/inicio.html', {'mensaje':'Datos incorrectos, intente de nuevo'})


     else:

          form = AuthenticationForm()
     
     return render(request, 'AppEntrega3Trueba/login.html', {'formulario':form})



def registro(request):

     if request.method == 'POST':

          form = UsuarioRegistro(request.POST)

          if form.is_valid():

               username = form.cleaned_data['username']
               form.save()
               return render(request, 'AppEntrega3Trueba/inicio.html', {'mensaje': 'Usuario creado.'})
     else:

          form = UsuarioRegistro()

     return render(request, 'AppEntrega3Trueba/registro.html',{'formulario':form})

@login_required
def editar_usuario(request):

     usuario = request.user

     if request.method == 'POST':

          form = FormularioEditar(request.POST)

          if form.is_valid():

               info = form.cleaned_data

               usuario.email = info['email']
               usuario.set_password(info['password1'])
               usuario.first_name = info['first_name']
               usuario.last_name = info['last_name']

               usuario.save()

               return render(request, 'AppEntrega3Trueba/inicio.html', {'mensaje':'Se ha editado correctamente tu usuario.'})

     else:

          form= FormularioEditar(initial= {
               'email':usuario.email,
               'first_name':usuario.first_name,
               'last_name':usuario.last_name,
          })
     
     return render(request,'AppEntrega3Trueba/editarPerfil.html', {'form':form, 'usuario':usuario})

def inicio(request):
    #return HttpResponse('Esta es la vista de bienvenida')
    return render(request,'AppEntrega3Trueba/inicio.html')


def jugadores(request): 
        if request.method == 'POST':
            
            mi_formulario = JugadorFormulario(request.POST)
            print(mi_formulario)

            if mi_formulario.is_valid:  
                 
                 
                informacion = mi_formulario.cleaned_data
      
                jugador = Jugador(nombre=informacion["nombre"], apellido=informacion["apellido"], alias=informacion["alias"], fecha_nacimiento=informacion["fecha_nacimiento"], edad=informacion["edad"], nacionalidad=informacion["nacionalidad"], posicion=informacion["posicion"], esta_retirado=informacion["esta_retirado"], goles=informacion["goles"], asistencias=informacion["asistencias"], cant_partidos=informacion["cant_partidos"], partidos_ganados=informacion["partidos_ganados"], partidos_empatados=informacion["partidos_empatados"], partidos_perdidos=informacion["partidos_perdidos"], palmares=informacion["palmares"] )
 
                jugador.save()
 
                return render(request, "AppEntrega3Trueba/inicio.html")
        
        else:

            mi_formulario = JugadorFormulario()
 
        return render(request,"AppEntrega3Trueba/jugadores.html", {'mi_formulario':mi_formulario})

def estadios(request):
    if request.method == 'POST':
            
            mi_formulario = EstadioFormulario(request.POST)
            print(mi_formulario)

            if mi_formulario.is_valid:
                 
                 
                informacion = mi_formulario.cleaned_data
      
                estadio = Estadio(nombre=informacion["nombre"], nombre_fant=informacion["nombre_fant"], capacidad=informacion["capacidad"], ubicacion=informacion["ubicacion"], club=informacion["club"], )

                estadio.save()
 
                return render(request, "AppEntrega3Trueba/inicio.html")
        
    else:
         mi_formulario = EstadioFormulario()
 
    return render(request,"AppEntrega3Trueba/estadios.html", {'mi_formulario':mi_formulario})

def clubes(request):
    if request.method == 'POST':
            
            mi_formulario = ClubFormulario(request.POST)
            print(mi_formulario)

            if mi_formulario.is_valid:
                 
                 
                informacion = mi_formulario.cleaned_data
      
                club = Club(nombre=informacion["nombre"], apodos=informacion["apodos"], socios=informacion["socios"], division=informacion["division"], fundacion=informacion["fundacion"], colores_principales=informacion["colores_principales"])

                club.save()
 
                return render(request, "AppEntrega3Trueba/inicio.html")
        
    else:
         mi_formulario = ClubFormulario()
 
    return render(request,"AppEntrega3Trueba/clubes.html", {'mi_formulario':mi_formulario})





def buscar_jugador(request):
     
     return render(request, 'AppEntrega3Trueba/buscarJugador.html')


def buscando_jugador(request):
     
     if request.GET['apellido']:
          apellido = request.GET['apellido']
          jugadores = Jugador.objects.filter(apellido__icontains=apellido)
     #respuesta = f'Buscando jugador con apellido {request.GET['apellido'] }'
          return render(request, 'AppEntrega3Trueba/resultadosBusquedaJugador.html', {'jugadores':jugadores, 'apellido':apellido})
     else:
          respuesta ="No se ha enviado ningún dato"

     return HttpResponse(respuesta)

def buscar_club(request):
     
     return render(request, 'AppEntrega3Trueba/buscarClub.html')

def buscando_club(request):
     if request.GET['nombre']:
          nombre = request.GET['nombre']
          clubes = Club.objects.filter(nombre__icontains=nombre)
          return render(request, 'AppEntrega3Trueba/resultadosBusquedaClub.html', {'clubes':clubes, 'nombre':nombre})
     else:
          respuesta ="No se ha enviado ningún dato"

     return HttpResponse(respuesta)


def buscar_estadio(request):
     
     return render(request, 'AppEntrega3Trueba/buscarEstadio.html')

def buscando_estadio(request):
     if request.GET['nombre_fant']:
          nombre_fant = request.GET['nombre_fant']
          estadios = Estadio.objects.filter(nombre_fant__icontains=nombre_fant)
          return render(request, 'AppEntrega3Trueba/resultadosBusquedaEstadio.html', {'estadios':estadios, 'nombre_fant':nombre_fant})
     else:
          respuesta ="No se ha enviado ningún dato"

     return HttpResponse(respuesta)



def leer_jugadores(request):

     jugador = Jugador.objects.all()

     contexto = {'jugadores': jugador}

     return render (request,'AppEntrega3Trueba/leerJugadores.html',contexto)

@login_required
def eliminar_jugadores(request, jugadorNombre):

     jugador = Jugador.objects.get(nombre=jugadorNombre)
     jugador.delete()

     jugadores = Jugador.objects.all()
     
     contexto = {'jugadores':jugadores}

     return render(request, "AppEntrega3Trueba/leerJugadores.html", contexto)


@login_required
def editar_jugadores(request, jugadorNombre):

     jugador = Jugador.objects.get(nombre=jugadorNombre)

     if request.method == 'POST':
          mi_formulario = JugadorFormulario(request.POST)
            

          if mi_formulario.is_valid():
                 
                 
               informacion = mi_formulario.cleaned_data
      

               jugador.nombre=informacion["nombre"]
               jugador.apellido=informacion["apellido"]
               jugador.alias=informacion["alias"]
               jugador.fecha_nacimiento=informacion["fecha_nacimiento"]
               jugador.edad=informacion["edad"]
               jugador.nacionalidad=informacion["nacionalidad"]
               jugador.posicion=informacion["posicion"]
               jugador.esta_retirado=informacion["esta_retirado"]
               jugador.goles=informacion["goles"]
               jugador.asistencias=informacion["asistencias"]
               jugador.cant_partidos=informacion["cant_partidos"]
               jugador.partidos_ganados=informacion["partidos_ganados"]
               jugador.partidos_empatados=informacion["partidos_empatados"]
               jugador.partidos_perdidos=informacion["partidos_perdidos"]
               jugador.palmares=informacion["palmares"]


               jugador.save()
 
               return render(request, "AppEntrega3Trueba/inicio.html")  
     else:
          mi_formulario = JugadorFormulario(initial={'nombre':jugador.nombre, 'apellido':jugador.apellido,
          'alias':jugador.alias,'fecha_nacimiento':jugador.fecha_nacimiento,'edad':jugador.edad,
          'nacionalidad':jugador.nacionalidad,'posicion':jugador.posicion,
          'esta_retirado':jugador.esta_retirado,'goles':jugador.goles,'asistencias':jugador.asistencias,
          'cant_partidos':jugador.cant_partidos,'partidos_ganados':jugador.partidos_ganados,
          'partidos_empatados':jugador.partidos_empatados,'partidos_perdidos':jugador.partidos_perdidos,
          'palmares':jugador.palmares})
 
     return render(request,"AppEntrega3Trueba/editarJugadores.html", {'mi_formulario':mi_formulario, 'nombre':jugadorNombre})


@login_required
def agregar_avatar(request):

     if request.method ==  'POST':

          form = AvatarFormulario(request.POST,request.FILES)

          if form.is_valid():

               usuarioAct = User.objects.get(username=request.user)

               avatar = Avatar(usuario=usuarioAct,imagen=form.cleaned_data['imagen'])
               avatar.save()

               return render(request, 'AppEntrega3Trueba/inicio.html')
          
     else:

          form =AvatarFormulario()

     return render(request, 'AppEntrega3Trueba/agregarAvatar.html', {'formulario':form})


class ListaClub(LoginRequiredMixin,ListView):

     model = Club

class DetalleClub(LoginRequiredMixin,DetailView):

     model = Club
     
class CrearClub(LoginRequiredMixin,CreateView):

     model = Club
     success_url = '/AppEntrega3Trueba/club/list'
     fields = ['nombre','apodos','socios','division','fundacion','colores_principales']

class ActualizarClub(LoginRequiredMixin,UpdateView):

     model = Club
     success_url = '/AppEntrega3Trueba/club/list'
     fields = ['nombre','apodos','socios','division','fundacion','colores_principales']

class BorrarClub(LoginRequiredMixin,DeleteView):

     model = Club
     success_url = '/AppEntrega3Trueba/club/list'



class ListaEstadio(ListView):

     model = Estadio

class DetalleEstadio(DetailView):

     model = Estadio
     
class CrearEstadio(CreateView):

     model = Estadio
     success_url = '/AppEntrega3Trueba/estadio/list'
     fields = ['nombre','nombre_fant','capacidad','ubicacion','club']

class ActualizarEstadio(UpdateView):

     model = Estadio
     success_url = '/AppEntrega3Trueba/estadio/list'
     fields = ['nombre','nombre_fant','capacidad','ubicacion','club']

class BorrarEstadio(DeleteView):

     model = Estadio
     success_url = '/AppEntrega3Trueba/estadio/list'



class ListaJugador(ListView):

     model = Jugador

class DetalleJugador(DetailView):

     model = Jugador
     
class CrearJugador(CreateView):

     model = Jugador
     success_url = '/AppEntrega3Trueba/jugador/list'
     fields = ['nombre','apellido','alias','fecha_nacimiento','edad','nacionalidad','posicion','esta_retirado','goles','asistencias','cant_partidos','partidos_ganados','partidos_empatados','partidos_perdidos','palmares']

class ActualizarJugador(UpdateView):

     model = Jugador
     success_url = '/AppEntrega3Trueba/jugador/list'
     fields = ['nombre','apellido','alias','fecha_nacimiento','edad','nacionalidad','posicion','esta_retirado','goles','asistencias','cant_partidos','partidos_ganados','partidos_empatados','partidos_perdidos','palmares']

class BorrarJugador(DeleteView):

     model = Jugador
     success_url = '/AppEntrega3Trueba/jugador/list'






