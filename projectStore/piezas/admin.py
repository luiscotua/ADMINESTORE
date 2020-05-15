from django.contrib import admin
from .models import Pieza, Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['id_categoria','nombre_categoria']
    search_fields = ('id_categoria','nombre_categoria')
    class Meta:
	     model = Categoria


class PiezaAdmin(admin.ModelAdmin):

    list_display = ['id_pieza','nombre_pieza','prioridad','precio','categoria','fecha_creacion','fecha_edicion']
    list_filter = ['prioridad','categoria__nombre_categoria']
    search_fields = ('nombre_pieza','fecha_creacion')
    class Meta:
	     model = Pieza


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pieza, PiezaAdmin)
