from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return str(self.nombre_categoria)


class Pieza(models.Model):
    ESTADO = (
        ('Ba', 'Baja'),
        ('Me', 'Media'),
        ('Al', 'Alta'),
    )

    id_pieza  = models.AutoField(primary_key=True)
    nombre_pieza = models.CharField(max_length=50, unique=True)
    prioridad = models.CharField(max_length=10, choices=ESTADO, default="Baja")
    precio = models.DecimalField(max_digits=8, default=0, decimal_places=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_edicion = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Pieza"
        verbose_name_plural = "Piezas"
    
    def __str__(self):
        return str(self.nombre_pieza)
