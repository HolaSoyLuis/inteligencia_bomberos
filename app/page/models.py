from django.db import models
# Create your models here.

class habitacion(models.Model):
	tipo_habitacion = (
		('0', 'sencillas'),
		('1', 'dobles'),
		)
	tipo = models.CharField(
		max_length= 1,
		choices = tipo_habitacion,
		default = '0',
		)
	descripcion = models.CharField(max_length = 150)
	numero = models.IntegerField(unique = True)
	ocupado = models.BooleanField(default=False)
	fecha = models.DateTimeField(auto_now_add = True)
	foto = models.ImageField(upload_to='media/', blank=True, null=True)
	'''
	def __str__(self):
		return '%s %s %s %s' % (self.numero,self.tipo,self.ocupado,self.descripcion)
	'''
	def __str__(self):
		return '%s' % (self.numero)

	def esta_ocupado(self):
		return self.ocupado

	def get_tipo_habitacion(self):
		return self.tipo

class cliente(models.Model):
	nombre = models.CharField(max_length = 150)
	dpi = models.CharField(max_length = 20)
	'''
	def __str__(self):
		return '%s %s' % (self.nombre,self.dpi)
	'''
	def __str__(self):
		return '%s' % (self.nombre)

class registro(models.Model):
	ccliente = models.ForeignKey(cliente)
	hhabitacion = models.ForeignKey(habitacion)
	fecha_ingreso = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return '%s %s' % (self.ccliente,self.hhabitacion)