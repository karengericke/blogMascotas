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
    
    path('crearDuenio', views.CrearDuenios.as_view(), name='crearDuenio'),
    
    path('crearRopita', views.CrearRopitas.as_view(), name='crearRopita'),
    path('listaMascotas/crear/', views.crearMascota, name='crearMascota'),

    path('nosotros/', views.nosotros, name="nosotros"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('login/', views.login_request, name="login"),

    path('registrar/', views.register, name='registrar'), 
    path('logout/', LogoutView.as_view(template_name='mascotasblog/logout.html'), name='logout'), 
    
    path('detalleDuenio/<pk>/', views.DetalleDuenios.as_view(), name='detalleDuenio'),
    path('modificarDuenio/<pk>/', views.ModificarDuenios.as_view(), name='modificarDuenio'),
    path('eliminarDuenio/<pk>/', views.BorrarDuenios.as_view(), name='eliminarDuenio'),
     
    path('detalleRopita/<pk>/', views.DetalleRopitas.as_view(), name='detalleRopita'),
    path('modificarRopita/<pk>/', views.ModificarRopitas.as_view(), name='modificarRopita'),
    path('eliminarRopita/<pk>/', views.BorrarRopitas.as_view(), name='eliminarRopita'), 

]