from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    registro_cantidad = models.IntegerField()
    codigo = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.marca)

class Categoria(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    utilidad = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    oficio = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    pais_fabricacion = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.area, self.utilidad)

class RegistroMercadeo(models.Model):
    cantidad_entrada = models.IntegerField()
    cantidad_vendida = models.IntegerField()
    ganancia = models.DecimalField(max_digits=10, decimal_places=2)
    stock_bajo = models.IntegerField()
    fecha_ultima_compra = models.DateField()
    transporte = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.transporte, self.ganancia)
