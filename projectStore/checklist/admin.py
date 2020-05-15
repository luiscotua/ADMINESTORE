from import_export.formats import base_formats
from import_export import resources
from import_export.admin import ExportMixin
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from django.contrib import admin
from .models import Visita, Checkpieza
from django.contrib.auth.models import User
from tiendas.models import Tienda, Municipio, Departamento
from piezas.models import Pieza

# Register your models here.
# class TiendaResource(resources.ModelResource):
#     tienda = fields.Field(attribute='tienda', widget=ForeignKeyWidget(Tienda, 'nombre_tienda'))
#     codigo_tienda = fields.Field(attribute='tienda', widget=ForeignKeyWidget(Tienda, 'codigo'))
#     municipio = fields.Field(attribute='tienda', widget=ForeignKeyWidget(Tienda, 'municipio__nombre_municipio'))
#     departamento = fields.Field(attribute='tienda', widget=ForeignKeyWidget(Tienda, 'municipio__departamento__nombre_departamento'))
#     region = fields.Field(attribute='tienda', widget=ForeignKeyWidget(Tienda, 'municipio__departamento__region__nombre_region'))
#     jefe_zona = fields.Field(attribute='tienda', widget=ForeignKeyWidget(Tienda, 'jefe_zona__username'))

#     class Meta:
#         import_id_fields = ('id_visita')
#         model = Visita
#         export_order = ('id_visita','fecha_visita','tienda','codigo_tienda','jefe_zona','municipio','departamento','region','observacion')
#         fields = ('id_visita','fecha_visita','tienda','codigo_tienda','jefe_zona','municipio','departamento','region','observacion')

class PiezaResource(resources.ModelResource):

    id_visita = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'id_visita'))
    fecha_visita = fields.Field(attribute='visita__fecha_visita')
    pieza = fields.Field(attribute='pieza', widget=ForeignKeyWidget(Pieza, 'nombre_pieza'))
    categoria = fields.Field(attribute='pieza', widget=ForeignKeyWidget(Pieza, 'categoria__nombre_categoria'))
    prioridad = fields.Field(attribute='pieza__prioridad')
    tienda = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'tienda__nombre_tienda'))
    codigo = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'tienda__codigo'))
    jefe_zona = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'tienda__jefe_zona__username'))
    municipio = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'tienda__municipio__nombre_municipio'))
    departamento = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'tienda__municipio__departamento__nombre_departamento'))
    region = fields.Field(attribute='visita', widget=ForeignKeyWidget(Visita, 'tienda__municipio__departamento__region__nombre_region'))

    class Meta:
        import_id_fields = ('id_checkpieza')
        model = Checkpieza
        export_order = ('id_visita','fecha_visita','tienda','codigo','jefe_zona','municipio','departamento','region','categoria','prioridad','pieza','cantidad','precio_total')
        fields = ('id_visita','fecha_visita','tienda','codigo','jefe_zona','municipio','departamento','region','categoria','prioridad','pieza','cantidad','precio_total')

class ThingInline(admin.TabularInline):
	model = Checkpieza
	min_num = 0
	extra = 4
	raw_id_fields = ('pieza',)
	verbose_name_plural = 'Chequeo de Piezas'
	suit_form_inlines_hide_original = True

class VisitaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['tienda']}),
        ('observacion', {'fields': ['observacion']}),
    ]

    list_display = ['tienda','fecha_visita','nombre','municipio','departamento','region','jefe_zona']
    list_filter = ['fecha_visita','tienda__codigo']
    search_fields = ('tienda__codigo','tienda__nombre_tienda')
    # resource_class = TiendaResource
    # list_select_related = (
    #     'category',
    # )
    inlines = [
        ThingInline,
	]

    def add_view(self, *args, **kwargs):
        self.fields = ('id_visita')
        return super(VisitaAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.fields = ('tienda',)
        return super(VisitaAdmin, self).change_view(*args, **kwargs)


    def nombre(self, obj):
        return obj.tienda.nombre_tienda

    def region(self, obj):
        return obj.tienda.municipio.departamento.region.nombre_region

    def municipio(self, obj):
        return obj.tienda.municipio

    def departamento(self, obj):
        return obj.tienda.municipio.departamento

    def jefe_zona(self, obj):
        return obj.tienda.jefe_zona.get_full_name()

    class Meta:
	    model = Visita


class CheckpiezaAdmin(ExportMixin, admin.ModelAdmin):

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

    list_display = ['id_checkpieza','visita','fecha_visita','pieza','cantidad','precio_total']
    resource_class = PiezaResource

    def fecha_visita(self, obj):
        return obj.visita.fecha_visita
    
    class Meta:
	     model = Checkpieza


admin.site.register(Visita, VisitaAdmin)
admin.site.register(Checkpieza, CheckpiezaAdmin)