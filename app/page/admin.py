from django.contrib import admin
from .models import habitacion,cliente,registro

# Register your models here.

admin.site.register(habitacion)
admin.site.register(cliente)
admin.site.register(registro)