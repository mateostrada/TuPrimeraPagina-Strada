from django.db import models

class Historia(models.Model):
    titulo = models.CharField(max_length=50, blank=True)
    historia = models.CharField(max_length=200, blank=True)
    conocer=models.CharField(max_length=15, null=True)
    def __str__(self):
        return f"{self.titulo}"

class Producto(models.Model):
    producto=models.CharField(max_length=50)
    cantidades_disponibles=models.IntegerField(null=True)
    precio=models.IntegerField(null=True)
    imagen = models.ImageField(upload_to="productos/", null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    codigo = models.IntegerField(unique=True)
    def __str__(self):
        return f"{self.producto}"
class Reseña(models.Model):
    autor = models.CharField(max_length=100)
    comentario = models.CharField(max_length=25)
    calificacion = models.IntegerField(null=True)

    def __str__(self):
        return f"opino que el servicio fue {self.comentario} y le doy un {self.calificacion}"
# Create your models here.
