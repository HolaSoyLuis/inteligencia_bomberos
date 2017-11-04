"""analisis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import vistaPrincipal,vistaHabitacion,listaHabitacion,vistaCliente,listaCliente,LoginView,CrearUsuarioView,EditarCliente,EditarHabitacion,vistaRegistro,listaRegistro
from .views import EliminarHabitacionView,EliminarClienteView,vistaPrincipal,vistaHabitacion,listaHabitacion,vistaCliente,listaCliente,LoginView,CrearUsuarioView
from django.contrib.auth.views import login,logout
from .views import listaHabitacionDisponible

from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    #url(r'^$', include('app.page.urls', namespace = 'page')),    
    url(r'^$', vistaPrincipal.as_view()),
	url(r'^principal$', vistaPrincipal.as_view(), name = 'principal'),
    url(r'^login$', LoginView.as_view(), name = 'login'),
    
	url(r'^habitacion$', vistaHabitacion.as_view(), name = 'habitacion'),
    url(r'^listaHabitacion$', listaHabitacion.as_view(), name = 'listaHabitacion'),
    url(r'^listaHabitacionDisponible$', listaHabitacionDisponible.as_view(), name = 'listaHabitacionDisponible'),
    url(r'^EliminarHabitacion/(?P<pk>\d+)/$', EliminarHabitacionView.as_view(), name = 'EliminarHabitacion'),
    url(r'^EliminarCliente/(?P<pk>\d+)/$', EliminarClienteView.as_view(), name = 'EliminarCliente'),
    

    url(r'^cliente$', login_required(vistaCliente.as_view()), name = 'cliente'),
    #url(r'^cliente$', vistaCliente.as_view(), name = 'cliente'),

    url(r'^listaCliente$', listaCliente.as_view(), name = 'listaCliente'),

    #url(r'^accounts/logout/$', logout, name = 'logout'),
	url(r'^logout/$', logout, {'template_name': 'principal.html'}, name = 'logout'),

    url(r'^CrearUsuario$', CrearUsuarioView.as_view(), name = 'CrearUsuario'),


    #updates
    url(r'^EditarCliente/(?P<pk>\d+)/', EditarCliente.as_view(), name = 'EditarCliente'),
    url(r'^EditarHabitacion/(?P<pk>\d+)/', EditarHabitacion.as_view(), name = 'EditarHabitacion'),


    #registro
    url(r'^registro$', vistaRegistro.as_view(), name = 'registro'),
    url(r'^listaRegistro$', listaRegistro.as_view(), name = 'listaRegistro'),
]
