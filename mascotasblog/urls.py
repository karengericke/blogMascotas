from django.urls import path
from django.urls.conf import include
from mascotasblog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('mascotas/', views.mascotas, name="mascotas"),
    path('listaMascotas/', views.listaMascotas, name='listaMascotas'),
    path('listaMascotas/crear/', views.crearMascota, name='crearMascota'),
    # path('ventas/', views.ventas, name="ventas"),
    # path('vendedores/', views.vendedores, name="vendedores"),
    # path('buscarmarca/', views.buscarmarca, name="buscarmarca"),
    # path('buscar/', views.buscar),
    # path('leermarcas/', views.leermarcas, name="leermarcas"),
    # path('borrarmarca/<id_marca>/', views.borrarmarca, name="borrarmarca"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('login/', views.login_request, name="login"),
    # path('listaVendedores/', views.ListarVendedores.as_view(), name="listar"),
    # path('detalle/<pk>/', views.DetalleVendedores.as_view(), name='Detalle'),
    # path('vendedores', views.CrearVendedores.as_view(), name='Nuevo'),
    # path('modificar/<pk>/', views.ModificarVendedores.as_view(), name='Modificar'),
    # path('eliminar/<pk>/', views.BorrarVendedores.as_view(), name='Eliminar'), 
    path('registrar/', views.register, name='registrar'), 
    path('logout/', LogoutView.as_view(template_name='mascotasblog/logout.html'), name='logout'), 

]