from django.shortcuts import render,get_object_or_404,redirect
from petra.models import Producto
from petra.models import Historia
from petra.models import Reseña
from django.http import Http404
from petra.forms import ReseñaForm
from petra.forms import HistoriaForm
from petra.forms import ProductoForm

def home(request):
    return render(request,"petra/index.html")


def producto_list(request):
    productos_query=Producto.objects.all()
    contexto={
        "producto_list":list(productos_query)
    }
    return render(request,"petra/producto_list.html",contexto)


def petra_historia(request):
    historia_query= Historia.objects.all()
    contexto={
        "petra_historia":historia_query
    }
    return render(request, "petra/petra_historia.html",contexto)


def petra_reseña(request):
    autor=request.GET.get("autor")
    reseña_query= Reseña.objects.all()
    if autor is not None:
        reseña_query= Reseña.objects.filter(
            autor__icontains=autor
        )
    contexto={
        "petra_reseña":list(reseña_query)
    }
    return render(request, "petra/petra_reseña.html",contexto)

def crear_reseña(request):
    if request.method=="POST":
        form= ReseñaForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect("petra_reseña")
    else:
        form=ReseñaForm()

    return render(request,"petra/petra_create.html",{"form":form})


def crear_conocer(request):
    if request.method=="POST":
        form= HistoriaForm(request.POST)
        if form.is_valid ():
            form.save()
            return redirect("petra_historia")
    else:
        form=HistoriaForm()

    return render(request,"petra/petra_historia_create.html",{"form":form})

def crear_producto(request):
    if request.method=="POST":
        form= ProductoForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("producto_list")
    else:
        form=ProductoForm()

    return render(request,"petra/producto_create.html",{"form":form})

# Create your views here.
