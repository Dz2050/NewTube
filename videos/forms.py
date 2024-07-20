from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, Video

def validar_extension(value):
    allowed_extensions = ['.mp4', '.mov', '.avi']
    if not value.lower().endswith(tuple(allowed_extensions)):
        raise ValidationError('Extensión de archivo no permitida')

def validar_id(value):
    if not value.isdigit() or len(value) != 5:
        raise ValidationError('El ID debe tener 5 caracteres numéricos.')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'id']

    id = forms.CharField(validators=[validar_id])    


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'nombre', 'extension', 'tamanio']
        labels = {
            'titulo': 'Título del vídeo',
            'nombre': 'Nombre del archivo',
            'extension': 'Extensión',
            'tamanio': 'Tamaño (MB)',
        }
        widgets = {
            'tamanio': forms.NumberInput(attrs={'min': 0, 'max': 3, 'step': 1.01, 'placeholder': 'Tamaño en MB (máximo 3)'})
        }

    extension = forms.CharField(validators=[validar_extension])