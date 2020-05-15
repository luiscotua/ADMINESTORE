from django.contrib import admin
from .models import Region, Departamento, Municipio, Tienda
from jet.filters import RelatedFieldAjaxListFilter #

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    
    list_display = ['id_region','nombre_region']
    class Meta:
	     model = Region

class DepartamentoaAdmin(admin.ModelAdmin):

    list_display = ['id_departamento','nombre_departamento','region']
    list_filter = ['region',]
    search_fields = ('nombre_departamento',)
    class Meta:
	     model = Departamento

class MunicipioAdmin(admin.ModelAdmin):

    list_display = ['id_municipio','nombre_municipio','departamento','region_municipio']
    list_filter = ['departamento',]
    search_fields = ('nombre_municipio','departamento')

    def region_municipio(self, obj):
        return obj.departamento.region

    class Meta:
	     model = Municipio

class TiendaAdmin(admin.ModelAdmin):

    list_display = ['id_tienda','codigo','nombre_tienda','region','departamento','municipio','jefe_zona']
    list_filter = ['municipio','jefe_zona']
    search_fields = ('codigo','nombre_tienda')

    def region(self, obj):
        return obj.municipio.departamento.region.nombre_region

    def departamento(self, obj):
        return obj.municipio.departamento.nombre_departamento

    class Meta:
	     model = Tienda


admin.site.register(Region, RegionAdmin)
admin.site.register(Departamento, DepartamentoaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Tienda, TiendaAdmin)