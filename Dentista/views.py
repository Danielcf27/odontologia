from django.shortcuts import render

def log(request):
    return render(request, "log.html")

def home(request):
    return render(request, "index.html")

def clientes(request):
    return render(request, "clientes.html")
def agregarCliente(request):
    return render (request, "agregar_cliente.html")   