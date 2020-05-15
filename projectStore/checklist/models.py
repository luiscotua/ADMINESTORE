from django.db import models
from tiendas.models import Tienda
from piezas.models import Pieza

# Create your models here.
class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    fecha_visita = models.DateField(auto_now_add=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.PROTECT)
    observacion = models.TextField(max_length=150, null=True, blank=True)
    pieza = models.ManyToManyField(Pieza, through='Checkpieza', related_name='visita_piezas',
    verbose_name='piezas_chekc', blank=False, through_fields=('visita','pieza'))

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
    
    def __str__(self):
        return str(self.id_visita)


class Checkpieza(models.Model):
    id_checkpieza = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(Pieza, related_name='checkpieza_pieza', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_total = models.FloatField(blank=True, null=True, editable=False)
    visita = models.ForeignKey(Visita, related_name='checkpieza_visita', on_delete=models.PROTECT)


    @property
    def multiplicar(self):
        return (self.cantidad * self.pieza.precio)

    def save(self):
        self.precio_total = self.multiplicar
        super (Checkpieza, self).save()

    class Meta:
        verbose_name = "Checkpieza"
        verbose_name_plural = "Checkpiezas"
    
    def __str__(self):
        return str(self.pieza)

#sumar = Checkpieza.objects.aggregate(precio_total=Sum('precio_instalacion') + Sum('pieza__precio'))
