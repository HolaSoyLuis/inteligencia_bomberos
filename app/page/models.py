from django.db import models
# Create your models here.

class bombero(models.Model):
    cui = models.CharField(max_length = 15)
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 8)
    foto = models.ImageField(upload_to='apps/servicios/static/profile_pictures/', blank = True)
    cargo_choices = (
        ('Oficial de servicio', 'Oficial de servicio'),
        ('Piloto de maquina', 'Piloto de maquina'),
        ('Camillero', 'Camillero'),
    )
    cargo = models.CharField(
        max_length = 20,
        choices = cargo_choices,
    )
    activo = models.BooleanField()
    registrado = models.DateTimeField(auto_now_add = True)

    def get_profile_picture(self):
        keyword = str(self.foto)
        key = keyword[22:]
        return key
    
    def __str__(self):
        return '%s %s' % (self.cui, self.nombre)

    def esta_activo(self):
        return self.activo