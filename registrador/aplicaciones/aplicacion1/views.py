
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto,Categoria,RegistroMercadeo

def home(request):
    # return HttpResponse("<h1>Bienvenido a su Gestion de Recursos</h1>")
    producto = Producto.objects.all()
    categoria = Categoria.objects.all()
    rm = RegistroMercadeo.objects.all()
    data = {"producto": producto, "categoria": categoria,"rm": rm}
    return render(request, "tablaR.html", data)


def producto_url(request):
    producto = Producto.objects.all()
    data = {"producto": producto}
    return render(request, "g_rPH1.html", data)

def categoria_url(request):
    categoria = Categoria.objects.all()
    data = {"categoria": categoria}
    return render(request, "g_rPH2.html", data)

def rm_url(request):
    rm = RegistroMercadeo.objects.all()
    data = {"rm": rm}
    return render(request, "g_rPH3.html", data)

def registrar_PRODUCTO(request):
    nombre = request.POST['txtNombre']
    marca = request.POST['txtMarca']
    registro_cantidad = request.POST['numRegistro_Cantidad']
    codigo = request.POST['txtCodigo']
    descuento = request.POST['numDescuento']
    precio = request.POST['numPrecio']
    peso = request.POST['numPeso']
    utilidad = request.POST['textUtilidad']
    area = request.POST['textArea']
    oficio = request.POST['textOficio']
    costo = request.POST['numCosto']
    pais_fabricacion = request.POST['textPaisF']
    cantidad_entrada = request.POST['numCantidadE']
    cantidad_vendida = request.POST['numCantidadV']
    ganancia = request.POST['numGanancia']
    stock_bajo = request.POST['numStockB']
    fecha_ultima_compra = request.POST['dateFechaU']
    transporte = request.POST['Transporte']

    registro1 = Producto.objects.create(
        nombre = nombre, marca = marca , registro_cantidad = registro_cantidad ,codigo = codigo ,descuento = descuento , precio = precio
    )
    registro2 = Categoria.objects.create(
        peso = peso, utilidad = utilidad , area = area ,oficio = oficio ,costo = costo , pais_fabricacion = pais_fabricacion
    )
    registro3 = RegistroMercadeo.objects.create(
        cantidad_entrada = cantidad_entrada, cantidad_vendida = cantidad_vendida , ganancia = ganancia ,stock_bajo = stock_bajo ,fecha_ultima_compra = fecha_ultima_compra , transporte = transporte
    )
    return redirect('/')

def eliminacion_PRODUCTO(request, codigo):
    registro1 = Producto.objects.get(codigo=codigo)
    registro1.delete()
    registro2 = Categoria.objects.get(codigo=codigo)
    registro2.delete()
    registro3 = RegistroMercadeo.objects.get(codigo=codigo)
    registro3.delete()
    return redirect('/')


def edicion_PRODUCTO(request, codigo):
    registro1 = Producto.objects.get(codigo=codigo)
    render(request, "edicionProducto.html", {"producto": registro1})
    registro2 = Categoria.objects.get(codigo=codigo)
    render(request, "edicionCategoria.html", {"categoria": registro2})
    registro3 = RegistroMercadeo.objects.get(codigo=codigo)
    render(request, "edicionRM.html", {"rm": registro3})
    
    return redirect('/')






