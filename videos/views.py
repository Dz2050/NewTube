from django.shortcuts import render, get_object_or_404, redirect
from .forms import VideoForm
from .models import Video
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError


def index(request):
    videos = Video.objects.all()
    return render(request, 'videos/index.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'videos/detail.html', {'video': video})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            id_usuario = request.POST['id']
            nombre_usuario = request.POST['nombre']
            cantidad_videos = request.POST['cantidad_videos'] 
            titulo_video = form.cleaned_data['titulo']
            nombre_video = form.cleaned_data['nombre']
            extension_video = request.POST['extension']
            tamanio_video = form.cleaned_data['tamanio']

            archivo_video = request.FILES.get('archivo_video')
            if archivo_video:
                if archivo_video.size > 3 * 1024 * 1024:
                    messages.error(request, 'El tamaño del archivo debe ser menor a 3 MB.')
                    return render(request, 'videos/upload.html', {'form': form})

                allowed_extensions = ['.mp4', '.mov', '.avi']
                if not archivo_video.name.lower().endswith(tuple(allowed_extensions)):
                    messages.error(request, 'Extensión de archivo no permitida.')
                    return render(request, 'videos/upload.html', {'form': form})
                else:
                    video.archivo_video = archivo_video

            try:
                usuario, created = Usuario.objects.get_or_create(id='id_usuario', defaults={'nombre': nombre_usuario})
            except IntegrityError:
                messages.error(request, 'Error al crear o obtener el usuario.')
                return render(request, 'videos/upload.html', {'form': form})

            video = Video(
                titulo=titulo_video,
                nombre=nombre_video,
                extension=extension_video,
                tamanio=tamanio_video,
                usuario=usuario
            )
            video.save()

            messages.success(request, '¡Video subido correctamente!')
            return redirect('index')

        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f'Error en el campo {field.label}: {error}')
            return render(request, 'videos/upload.html', {'form': form})

    else:
        form = VideoForm()

    return render(request, 'videos/upload.html', {'form': form})

@login_required
def profile(request):
    user = get_object_or_404(Usuario, id=request.user.id)
    return render(request, 'videos/profile.html', {'user': user})

def search(request):
    query = request.GET.get('q')
    if query:
        video_list = Video.objects.filter(titulo__icontains=query)
        paginator = Paginator(video_list, 10)
        page = request.GET.get('page')
        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            videos = paginator.page(1)
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)

    else:
        videos = []                

    return render(request, 'videos/search.html', {'videos': videos, 'query': query})

def ver_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'videos/detail.html', {'video': video})