from django.shortcuts import render

#para el logueo de los usuarios
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import FormView
#estas tres lineas

from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .models import bombero
from .forms import bomberoForm, bombero_form

# Create your views here.

#vista principal
class vistaPrincipal(TemplateView):
	template_name = 'principal.html'

#habitacion
class vistaHabitacion(CreateView):
	template_name = 'bomberox.html'
	form_class =  bombero_form
	success_url = 'principal'

class listaHabitacion(ListView):
	template_name = 'listaBombero.html'
	model = bombero

	def get_queryset(self):
		return bombero.objects.all()

class EditarHabitacion(UpdateView):
	template_name = 'bombero.html'
	model = bombero
	form_class = bomberoForm
	success_url = 'listaBombero'

class EliminarHabitacionView(DeleteView):
	template_name = 'eliminar.html'
	model = bombero
	success_url = 'principal'
#end habitacion

#crear usuarios
class CrearUsuarioView(CreateView):
	model = User
	template_name = 'CrearUsuario.html'
	form_class = UserCreationForm
	success_url = 'principal'

#login
class LoginView(FormView):
	template_name = 'login.html'
	form_class = AuthenticationForm
	success_url = 'principal'

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)
#end login
