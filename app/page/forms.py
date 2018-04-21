from django import forms
from .models import bombero

class bomberoForm(forms.ModelForm):
	class Meta:
		model = bombero
		fields = '__all__'

class bombero_form(forms.ModelForm):
    class Meta:
        model = bombero
        fields = (
            'cui',
            'nombre',
            'edad',
            'direccion',
            'telefono',
            'foto',
            'cargo',
            'activo',
        )

        labels = {
            'cui': 'Cui',
            'nombre': 'Nombre',
            'edad': 'Edad',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'foto': 'Foto',
            'cargo': 'Cargo',
            'activo': 'Esta activo',
        }