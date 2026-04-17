from django.urls import path
from petra.views import *

urlpatterns = [
    path("",home, name="home"),
    path("productos/",producto_list,name="producto_list"),
    path("historia/",petra_historia,name="petra_historia"),
    path("reseña/",petra_reseña,name="petra_reseña"),
    path("reseña/crear/", crear_reseña, name="petra_create"),
    path("historia/crear/", crear_conocer, name="crear_conocer"),
    path("producto/crear/",crear_producto,name="crear_producto"),
]
