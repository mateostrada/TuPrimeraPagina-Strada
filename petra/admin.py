from django.contrib import admin
from petra.models import Producto
from petra.models import Historia
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=("producto","cantidades_disponibles","precio")

    search_fields=("preducto",)

    ordering=("producto","precio")

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display=("conocer",)

    search_fields=("conocer",)

    ordering=("conocer",)
# Register your models here.
