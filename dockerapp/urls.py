from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from dockerapp.models import TestingDocker
from django.conf import settings
from django.conf.urls.static import static


def dockerview(request):
    t = (TestingDocker.objects.all())
    print('---->',t)
    return HttpResponse(t)

urlpatterns = [
    path("", dockerview)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
