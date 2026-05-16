from django.urls import path
from petra.views import *

urlpatterns = [
    path("",home, name="home"),
    #path("productos/",producto_list,name="producto_list"),
    path("historia/",petra_historia,name="petra_historia"),
    path("reseña/",petra_reseña,name="petra_reseña"),
    path("reseña/crear/", crear_reseña, name="petra_create"),
    path("historia/crear/", crear_conocer, name="crear_conocer"),
    #path("producto/crear/",crear_producto,name="crear_producto"),
    path("productos/", ProductoListView.as_view(), name="producto_list"),
    path("productos/<int:pk>/", ProductoDetailView.as_view(), name="producto_detail"),
    path("productos/crear/", ProductoCreateView.as_view(), name="producto_create"),
    path("productos/<int:pk>/editar/", ProductoUpdateView.as_view(), name="producto_update"),
    path("productos/<int:pk>/eliminar/", ProductoDeleteView.as_view(), name="producto_delete"),
]
