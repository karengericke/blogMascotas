from django.urls import path
from django.urls.conf import include
from mascotasblog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('mascotas/', views.mascotas, name="mascotas"),
    
    path('listaMascotas/', views.listaMascotas, name='listaMascotas'),
    path('listaRopita/', views.ListarRopitas.as_view(), name='listaRopita'), 
    path('listaDuenios/', views.ListarDuenios.as_view(), name='listaDuenios'), 
    
    path('crearDuenio/', views.crearDuenio, name="crearDuenio"),
    path('crearDuenio', views.CrearDuenios.as_view(), name='crearDuenio'),
    path('listaMascotas/crear/', views.crearMascota, name='crearMascota'),

    path('nosotros/', views.nosotros, name="nosotros"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('login/', views.login_request, name="login"),

    path('registrar/', views.register, name='registrar'), 
    path('logout/', LogoutView.as_view(template_name='mascotasblog/logout.html'), name='logout'), 
    
    path('detalle/<pk>/', views.DetalleDuenios.as_view(), name='Detalle'),
    path('modificar/<pk>/', views.ModificarDuenios.as_view(), name='Modificar'),
    path('eliminar/<pk>/', views.BorrarDuenios.as_view(), name='Eliminar'), 

]