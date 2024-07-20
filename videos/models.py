from django.db import models
import uuid

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.nombre


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    archivo_video = models.FileField(upload_to='videos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    extension = models.CharField(max_length=5)
    tamanio = models.FloatField()

    def __str__(self):
        return self.titulo


class UsuarioVideo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    fecha_visualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.video.titulo}"

