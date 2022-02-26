from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from mascotasblog.models import *
from mascotasblog.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# vistas generales de la app.

def inicio(req):
    return render(req, "mascotasblog/inicio.html")

def mascotas(request):
    return render(request, "mascotasblog/mascotas.html")

def nosotros(req):
    return render(req, "mascotasblog/quienessomos.html")

def blogpost(req):
    return render(req, "mascotasblog/blogpost.html") 

def buscarMascota(request):
    
    return render(request, "mascotasblog/busquedamarca.html/")


def listaMascotas(request):
    error_edad = None
    mascotas = None
    error_nombre = None
    error_raza = None
    error_trucos = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        edad = request.GET.get('edad',None)
        raza = request.GET.get('raza','')
        trucos = request.GET.get('trucos',None)
        if nombre == '' and edad == '' and raza == '' and trucos == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            mascotas = Mascota.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha():
                mascotas = Mascota.objects.filter(nombre = nombre)
            else:
                error_nombre = 'Debe ingresar un nombre válido'
        
        elif raza:
            if raza.replace(' ','').isalpha():
                mascotas = Mascota.objects.filter(raza = raza)
            else:
                error_raza = 'Debe ingresar una raza válida'
                
        elif edad:
            try: 
                edad = int(edad)
                mascotas = Mascota.objects.filter(edad = edad)
            except:
                error_edad = 'Debe ingresar una edad válida'  
                
        elif trucos:
            if trucos.replace(' ','').isalpha(): 
                mascotas = Mascota.objects.filter(trucos = trucos)
            else:
                error_trucos = 'Debe ingresar una truco válido' 
    
                         
    return render(request, 'mascotasblog/listaMascotas.html', {'mascotas': mascotas, 'error_nombre': error_nombre, 'error_raza': error_raza, 'error_edad': error_edad, 'error_trucos': error_trucos})

@login_required
def crearMascota(request):
    if request.method == 'POST':
        formulario = fMascotas(request.POST)
        
        if formulario. is_valid():
            datos_mascotas = formulario.cleaned_data
            mascota = Mascota(nombre = datos_mascotas['nombre'], edad = datos_mascotas['edad'], raza = datos_mascotas['raza'], trucos = datos_mascotas['trucos'])
            mascota.save()
            return redirect('listaMascotas')
    formulario = fMascotas()
        
    return render(request, 'mascotasblog/crearMascota.html', {'formulario': formulario})


#########################################################################################################################################

class ListarDuenios(LoginRequiredMixin, ListView):
    model = Duenio
    template_name="mascotasblog/listaDuenios.html" 
    
class CrearDuenios(LoginRequiredMixin, CreateView):
    model = Duenio
    success_url="/mascotasblog/listaDuenios/"
    fields=["nombre", "apellido", "edad"] 
    template_name ="mascotasblog/crearDuenio.html"
    
class DetalleDuenios(LoginRequiredMixin, DetailView):
    model= Duenio
    template_name="mascotasblog/detalleDuenio.html"

class ModificarDuenios(LoginRequiredMixin, UpdateView):
    model= Duenio
    success_url="/mascotasblog/listaDuenios/"
    fields=['nombre', 'apellido', 'edad']
    template_name ="mascotasblog/editarDuenio.html"

class BorrarDuenios(LoginRequiredMixin, DeleteView):
    model= Duenio
    success_url="/mascotasblog/listaDuenios/"
    template_name ="mascotasblog/borrarDuenio.html"

#########################################################################################################################################

class ListarRopitas(LoginRequiredMixin, ListView):
    model = Ropita
    template_name="mascotasblog/listaRopita.html" 
class CrearRopitas(LoginRequiredMixin, CreateView):
    model = Ropita
    success_url="/mascotasblog/listaRopita/"
    fields=["nombre", "marca", "color", "precio"] 
    template_name ="mascotasblog/crearRopita.html"
    
class DetalleRopitas(DetailView):
    model= Ropita
    template_name="mascotasblog/detalleRopita.html"

class ModificarRopitas(UpdateView):
    model= Ropita
    success_url="/mascotasblog/listaRopita/"
    fields=["nombre", "marca", "color", "precio"] 
    template_name ="mascotasblog/editarRopita.html"

class BorrarRopitas(DeleteView):
    model= Ropita
    success_url="/mascotasblog/listaRopita/"
    template_name ="mascotasblog/borrarRopita.html"
    
#########################################################################################################################################


def login_request(request):

    if (request.method == "POST"):
            
        form = AuthenticationForm(request, data = request.POST)
                    
        if form.is_valid():
            data = form.cleaned_data
                    
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)   
                    
                return render(request,"mascotasblog/inicio.html",  {"mensaje":f"Bienvenido {user.get_username()} Que tal tu dia 😎"} )
                  
            else:

                return render(request,"mascotasblog/inicio.html", {"mensaje":"Error, datos incorrectos"} )

        else:                        
            return render(request,"mascotasblog/inicio.html" ,  {"mensaje":"Error, El usuario no existe o la contraseña esta mal 😥"})
    else:
      form = AuthenticationForm()
      return render(request,"mascotasblog/login.html", {'form':form} )

def register(request):

    if (request.method == "POST"):

        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"mascotasblog/inicio.html",   {"mensaje": "Se ha creado exitosamente su usuario, Bienvenido a bordo marinero 😎"} )

    else:
        form = UserCreationForm()       
        

    return render(request,"mascotasblog/registro.html" ,  {"form":form})