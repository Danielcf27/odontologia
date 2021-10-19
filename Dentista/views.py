from django.shortcuts import render

def log(request):
    return render(request, "log.html")

def home(request):
    return render(request, "index.html")

def clientes(request):
    return render(request, "clientes.html")

def agregarCliente(request):
    return render (request, "agregar_cliente.html")  

def productos(request):
    return render(request, "productos.html")

def agregaProducto(request):
    return render(request, "agregarProducto.html")