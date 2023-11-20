from django.urls import path
from .views import producto_url, categoria_url, rm_url, registrar_PRODUCTO, eliminacion_PRODUCTO, edicion_PRODUCTO


urlpatterns = [
    path('producto_url/',producto_url),
    path('categoria_url/',categoria_url),
    path('rm_url/',rm_url),
    path('registrar_PRODUCTO/', registrar_PRODUCTO),
    path('edicion_PRODUCTO/<codigo>', edicion_PRODUCTO),
    path('eliminacion_PRODUCTO/<codigo>', eliminacion_PRODUCTO),

]