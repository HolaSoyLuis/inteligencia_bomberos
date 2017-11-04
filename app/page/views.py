from django.shortcuts import render

#para el logueo de los usuarios
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import FormView
#estas tres lineas

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .models import habitacion,cliente,registro
from .forms import habitacionForm,clienteForm,registroForm

# Create your views here.

#vista principal
class vistaPrincipal(TemplateView):
	template_name = 'principal.html'




#habitacion
class vistaHabitacion(CreateView):
	template_name = 'habitacion.html'
	form_class =  habitacionForm
	success_url = reverse_lazy('page:principal')

class listaHabitacion(ListView):
	template_name = 'listaHabitacion.html'
	model = habitacion

	def get_queryset(self):
		return habitacion.objects.all()

class EditarHabitacion(UpdateView):
	template_name = 'habitacion.html'
	model = habitacion
	form_class = habitacionForm
	success_url = reverse_lazy('page:listaHabitacion')

class EliminarHabitacionView(DeleteView):
	template_name = 'eliminar.html'
	model = habitacion
	success_url = reverse_lazy('page:principal')

class listaHabitacionDisponible(ListView):
	template_name = 'listaHabitacionDisponible.html'
	model = habitacion

	def get_queryset(self):
		return habitacion.objects.all()
#end habitacion




#cliente
class vistaCliente(CreateView):
	template_name = 'cliente.html'
	form_class =  clienteForm
	success_url = reverse_lazy('page:principal')

class listaCliente(ListView):
	template_name = 'listaCliente.html'
	model = cliente

	def get_queryset(self):
		return cliente.objects.all()

class EditarCliente(UpdateView):
	template_name = 'cliente.html'
	model = cliente
	form_class = clienteForm
	success_url = reverse_lazy('page:listaCliente')

class EliminarClienteView(DeleteView):
	template_name = 'eliminar.html'
	model = cliente
	success_url = reverse_lazy('page:principal')
#end cliente






#crear usuarios
class CrearUsuarioView(CreateView):
	model = User
	template_name = 'CrearUsuario.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('page:principal')

#login
class LoginView(FormView):
	template_name = 'login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('page:principal')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)
#end login











#registro
class vistaRegistro(CreateView):
	template_name = 'registro.html'
	form_class =  registroForm
	success_url = reverse_lazy('page:principal')

class listaRegistro(ListView):
	template_name = 'listaRegistro.html'
	model = registro

	def get_queryset(self):
		return registro.objects.all()
'''
	def ocupar_habitacion():
		value = registro.objects.count()
		value2 = registro.objects.get(value)
		habitacion.objects.filter(id = value2.id).update(ocupado = True)
'''



