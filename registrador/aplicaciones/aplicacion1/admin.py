from django.contrib import admin
from .models import Producto, Categoria, RegistroMercadeo

# class ProductoAdmin(admin.ModelAdmin):
#     list_display = ['nombre','marca','registro_cantidad','codigo','descuento','precio']

# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ['peso','utilidad','area','oficio','costo','pais_fabricacion']

# class RMAdmin(admin.ModelAdmin):
#     list_display = ['cantidad_entrada','cantidad_vendida','ganancia','stock_bajo','fecha_ultima_compra','transporte']

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(RegistroMercadeo)




# Register your models here.
