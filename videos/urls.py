from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),  # Detalles del video
    path('subir/', views.upload_video, name='upload_video'),  # Página de subida de video
    path('perfil/', views.profile, name='profile'),  # Página de perfil
    path('buscar/', views.search, name='search'),  # Página de búsqueda
    path('ver/', views.ver_video, name='ver_video'),
]