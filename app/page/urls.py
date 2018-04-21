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
from django.urls import path, include
from .views import vistaPrincipal,vistaHabitacion,listaHabitacion,LoginView,CrearUsuarioView,EditarHabitacion
from .views import EliminarHabitacionView,LoginView,CrearUsuarioView
from django.contrib.auth.views import login,logout
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistaPrincipal.as_view()),
    path('principal', vistaPrincipal.as_view(), name = 'principal'),
    path('login', LoginView.as_view(), name = 'login'),
    
    path('bombero', vistaHabitacion.as_view(), name = 'bombero'),
    path('listaBombero', listaHabitacion.as_view(), name = 'listaBombero'),
    path('EditarBombero/(?P<pk>\d+)/', EditarHabitacion.as_view(), name = 'EditarBombero'),
    path('EliminarBombero/(?P<pk>\d+)/', EliminarHabitacionView.as_view(), name = 'EliminarBombero'),
    
    path('CrearUsuario', CrearUsuarioView.as_view(), name = 'CrearUsuario'),
	path('logout', logout, {'template_name': 'principal.html'}, name = 'logout'),
    #registro
]
