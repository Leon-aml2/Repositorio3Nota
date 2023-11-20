"""URL Principal """
from django.contrib import admin
from django.urls import path, include
from aplicaciones.aplicacion1.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('aplicaciones.aplicacion1.urls')),
    path('',home),
]
