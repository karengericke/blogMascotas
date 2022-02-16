from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mascotasblog.models import *
from mascotasblog.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# vistas generales de la app.

def inicio(req):
    return render(req, "mascotasblog/inicio.html")

def marcas(request):
    miformulario = fMarcas(request.POST)
    print(miformulario)

    if miformulario.is_valid():
        info = miformulario.cleaned_data
        marca = marcasvehiculo (marca=info['marca'], serie=info['serie'], ano_fabricacion=info['ano_fabricacion'], pais_fabricacion=info['pais_fabricacion'],)
        marca.save()

        return render(request, "mascotasblog/marcas.html")
    
    else:
        miformulario = fMarcas()
    
    return render (request, "mascotasblog/marcas.html", {"miformulario":miformulario})

def ventas(request):
    miformulario2 = fVentas(request.POST)
    print(miformulario2)

    if miformulario2.is_valid():
        info = miformulario2.cleaned_data
        ventas = venta (vehiculo_vendido=info['vehiculo_vendido'], precio=info['precio'], garantia_tiempo=info['garantia_tiempo'], garantia_kilometros=info['garantia_kilometros'],)
        ventas.save()

        return render(request, "mascotasblog/ventas.html")
    
    else:
        miformulario2 = fVentas()
    
    return render (request, "mascotasblog/ventas.html", {"miformulario2":miformulario2})

def vendedores(request):
    miformulario3 = fVendedores(request.POST)
    print(miformulario3)

    if miformulario3.is_valid():
        info = miformulario3.cleaned_data
        vendedor = vendedore (nombre_vendedor=info['nombre_vendedor'], apellido_vendedor=info['apellido_vendedor'], email_vendedor=info['email_vendedor'], sucursal=info['sucursal'],)
        vendedor.save()

        return render(request, "mascotasblog/vendedores.html/")
    
    else:
        miformulario3 = fVendedores()
    
    return render (request, "mascotasblog/vendedores.html", {"miformulario3":miformulario3})

def buscarmarca(request):
    
    return render(request, "mascotasblog/busquedamarca.html/")

def buscar(request):

    if request.GET ["marca"]:
        marcas = request.GET["marca"]
        marca = marcasvehiculo.objects.filter(marca__icontains=marcas)

        return render (request, "mascotasblog/resultadosbusqueda.html", {"marca": marca})
        
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def leermarcas(request):
    marca = marcasvehiculo.objects.all()
    contexto = {"marca": marca}
    return render (request, "mascotasblog/leermarcas.html", contexto)

def borrarmarca(request, id_marca):
    marca= marcasvehiculo.objects.get(id=id_marca)
    marca.delete()

    marcas= marcasvehiculo.objects.all()
    contexto={"marcas":marcas}

    return render(request, "mascotasblog/leermarcas.html", contexto)

def nosotros(req):
    return render(req, "mascotasblog/quienessomos.html")

def blogpost(req):
    return render(req, "mascotasblog/blogpost.html") 

class ListarVendedores(ListView):
    model= vendedore
    template_name="mascotasblog/listar.html" 


class DetalleVendedores(DetailView):
    model= vendedore
    template_name="mascotasblog/detalles.html"

class CrearVendedores(CreateView):
    model= vendedore
    success_url="/mascotasblog/listaVendedores/"
    fields=["nombre_vendedor", "apellido_vendedor", "email_vendedor", "sucursal"] 
    template_name ="mascotasblog/vendedores.html"

class ModificarVendedores(UpdateView):
    model= vendedore
    success_url="/mascotasblog/listaVendedores/"
    fields=['nombre_vendedor', 'apellido_vendedor', 'email_vendedor', 'sucursal']
    template_name ="mascotasblog/editar.html"

class BorrarVendedores(DeleteView):
    model= vendedore
    success_url="/mascotasblog/listaVendedores/"
    template_name ="mascotasblog/borrar.html"

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