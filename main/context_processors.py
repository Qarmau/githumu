# main/context_processors.py

from .models import BackgroundImage

def background_images(request):
    images = BackgroundImage.objects.filter(is_active=True)
    return {'background_images': images}