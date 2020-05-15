from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
    
    def __str__(self):
        return str(self.nombre_region)


class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
    
    def __str__(self):
        return str(self.nombre_departamento)

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre_municipio = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
    
    def __str__(self):
        return str(self.nombre_municipio)


class Tienda(models.Model):
    id_tienda  = models.AutoField(primary_key=True)
    codigo = models.PositiveIntegerField(default=000, unique=True)
    nombre_tienda = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    jefe_zona = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"
    
    def __str__(self):
        return str(self.codigo)
