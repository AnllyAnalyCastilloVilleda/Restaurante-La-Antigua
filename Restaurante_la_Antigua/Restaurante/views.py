from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect("/inicio")

def menu(request):
    return render(request,"menu.html")

def pedidos(request):
    return render(request,"pedidos.html")

def inicio(request):
    return render(request, "inicio.html")