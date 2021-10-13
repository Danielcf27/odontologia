from django.shortcuts import render

def log(request):
    return render(request, "log.html")

def home(request):
    return render(request, "index.html")
