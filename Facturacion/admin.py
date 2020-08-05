from django.contrib import admin
# Register your models here.
from Facturacion.models import Factura, DetalleFactura, Cliente, Producto
class ProductoAdmin(admin.ModelAdmin):
    fields = ['descripcion','precio','stock', 'iva']
    list_display = ('descripcion','precio', 'stock','iva')
    search_fields = ('descripcion',)

class ClienteAdmin(admin.ModelAdmin):
    fields = ['nombre','direccion','producto']
    list_display = ('nombre','direccion')
    search_fields = ('nombre',)

class FacturaAdmin(admin.ModelAdmin):
    fields = ['cliente','fecha','total']
    list_display = ('cliente','fecha','total')
    search_fields = ('cliente',)

class DetalleFacturaAdmin(admin.ModelAdmin):
    fields = ['factura','producto','cantidad','precio','subtotal']
    list_display = ('factura','producto','cantidad','precio','subtotal')
    search_fields = ('producto',)
admin.site.register(DetalleFactura,DetalleFacturaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Cliente,ClienteAdmin)