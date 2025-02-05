
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tickets.views import ClienteViewSet, EventoViewSet, IngressoViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'ingrssos', IngressoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)), 
]
