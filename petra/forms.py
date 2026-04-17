from django import forms
from petra.models import Reseña
from petra.models import Historia
from petra.models import Producto

class ReseñaForm(forms.ModelForm):
    class Meta:
        model= Reseña
        fields=("autor","comentario","calificacion")
        widgets={
            "autor": forms.TextInput(attrs={"class":"form-control"}),
            "comentario": forms.TextInput(attrs={"class":"form-control"}),
            "calificacion": forms.NumberInput(attrs={"class":"form-control"}),
        }


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = ( "conocer",)
        widgets = {
            "conocer": forms.TextInput(attrs={"class":"form-control"}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields=("producto","cantidades_disponibles","precio")
        widgets={
            "producto": forms.TextInput(attrs={"class":"form-control"}),
            "cantidades_disponibles": forms.NumberInput(attrs={"class":"form-control"}),
            "precio": forms.NumberInput(attrs={"class":"form-control"}),
        }
