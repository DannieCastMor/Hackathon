from django import forms
from bibliotecaDB.models import usuarios


class FormularioUsuarios(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'