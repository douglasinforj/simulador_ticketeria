
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tickets.views import ClienteViewSet, EventoViewSet, IngressoViewSet

from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'ingressos', IngressoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
