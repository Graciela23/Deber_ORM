from Facturacion.models import Producto,Cliente,Factura,DetalleFactura
#INSERTAR PRODUCTO
prod1= Producto(descripcion='Aceite Girazol',precio=0.50,stock=500)
prod1.save()
prod2= Producto(descripcion='Coca cola',precio=1.35,stock=230)
prod2.save()
prod3= Producto(descripcion='Leche',precio=1.24,stock=50)
prod3.save()
prod4= Producto(descripcion='Jugo de naranja',precio=1.45,stock=50)
prod4.save()
Producto.objects.create(descripcion='Papas fritas',precio=0.45,stock=1500)
Producto.objects.create(descripcion='Galleta ricas',precio=0.94,stock=1050)
Producto.objects.create(descripcion='galleta de chocolate',precio=0.45,stock=1050)
Producto.objects.create(descripcion='agua',precio=0.65,stock=100)
#---------------------------------------------------------------------------------------------#
#CLIENTE
cli1=Cliente(nombre='Graciela Guevara',ruc='456789123',direccion='milagro')
cli1.producto_set=prod3
cli1.save()
cli2=Cliente(nombre='Guevara',ruc='74575757',direccion='av los vergeles')
cli2.producto_set=prod4
cli2.save()
cli3=Cliente(nombre='Maria jose',ruc='75854243',direccion='av juan montalvo')
cli3.producto_set=prod1
cli3.save()
cli4=Cliente(nombre='Juana gabriel',ruc='797865435',direccion='milagro')
cli4.producto_set=prod1
cli4.save()
cli=Cliente.objects.create(nombre='nancy rosario',ruc='124852001',direccion='milagro')
cli6=Cliente.objects.create(nombre='rosa elvira',ruc='1234560111',direccion='av los vergeles')
cli7=Cliente.objects.create(nombre='maritza lopez',ruc='1234567011',direccion='av los vergeles')
cli8=Cliente.objects.create(nombre='ginger luna',ruc='59785521',direccion='av los vergeles')
cli9=Cliente.objects.create(nombre='jesus suarez',ruc='5454654654',direccion='av los vergeles')
#---------------------------------------------------------------------------------------------#
#FACTURA
fact1=Factura(cliente=cli9,fecha='2015-02-16',total=500.00)
fact1.save()
fact2=Factura(cliente=cli8,fecha='2016-03-12',total=650.00)
fact2.save()
fact3=Factura(cliente=cli7,fecha='2017-02-14',total=15.00)
fact3.save()
fact4=Factura(cliente=cli6,fecha='2016-07-17',total=258.00)
fact4.save()
fact5=Factura.objects.create(cliente=cli4,fecha='2020-03-01',total=1440.00)
fact6=Factura.objects.create(cliente=cli3,fecha='2019-04-02',total=45.00)
fact7=Factura.objects.create(cliente=cli4,fecha='2018-05-03',total=10.00)
fact8=Factura.objects.create(cliente=cli1,fecha='2017-06-04',total=10.00)
#---------------------------------------------------------------------------------------------#
#DETALLEFACTURA
detalle1=DetalleFactura(factura=fact1,producto=prod3,cantidad=5,precio=10,subtotal=50)
detalle1.save()
detalle2=DetalleFactura(factura=fact4,producto=prod2,cantidad=2,precio=10,subtotal=20)
detalle2.save()
detalle3=DetalleFactura(factura=fact2,producto=prod1,cantidad=2,precio=15,subtotal=30)
detalle3.save()
detalle4=DetalleFactura(factura=fact4,producto=prod1,cantidad=3,precio=10,subtotal=30)
detalle4.save()
detalle5=DetalleFactura.objects.create(factura=fact5,producto=prod2)
detalle6=DetalleFactura.objects.create(factura=fact1,producto=prod1)
detalle7=DetalleFactura.objects.create(factura=fact6,producto=prod2)
detalle8=DetalleFactura.objects.create(factura=fact2,producto=prod3)
#---------------------------------------------------------------------------------------------#
#MODIFICAR
#PRODUCTO
prod1 = Producto.objects.get(id=1)
prod1.precio=10.50
prod1.save()
prod2 = Producto.objects.get(id=2)
prod2.precio=10.50
prod2.save()
Producto.objects.filter(id=3).update(precio=10.50)
Producto.objects.filter(id=4).update(precio=10.50)
#CLIENTE
cli1 = Cliente.objects.get(id=1)
cli1.direccion='los vergeles'
cli1.save()
cli2 = Cliente.objects.get(id=2)
cli2.direccion='los vergeles'
cli2.save()
Cliente.objects.filter(id=3).update(direccion='av las americas')
Cliente.objects.filter(id=4).update(direccion='av las americas')
#FACTURA
fact1 = Factura.objects.get(id=2)
fact1.total=20.50
fact1.save()
fact2 = Factura.objects.get(id=3)
fact2.total=35.85
fact2.save()
Factura.objects.filter(id=2).update(total=17.25)
Factura.objects.filter(id=1).update(total=12.89)

#M FACTURA
fact1 = Factura.objects.get(id=1)
fact1.total=7.85
fact1.save()
fact2 = Factura.objects.get(id=2)
fact2.total=15.75
fact2.save()
Factura.objects.filter(id=3).update(total=5.85)
Factura.objects.filter(id=4).update(total=3.35)
#DETALLEFACTURA
det1 = DetalleFactura.objects.get(id=1)
det1.cantidad=3
det1.save()
det2 = DetalleFactura.objects.get(id=2)
det2.cantidad=2
det2.save()
DetalleFactura.objects.filter(id=3).update(cantidad=10)
DetalleFactura.objects.filter(id=4).update(cantidad=15)
#---------------------------------------------------------------------------------------------#
#ELIMINAR PRODUCTO
prod=Producto.objects.get(id=1)
prod.delete()
Producto.objects.filter(id=2).delete()
cli=Cliente.objects.get(id=1)
cli.delete()
cli.Cliente.objects.filter(id=2).delete()
#ELIMINAR FACTURA
fact=Factura.objects.get(id=1)
fact.delete()
Factura.objects.filter(id=2).delete()
#ELIMINAR  DETALLEFACTURA
det1=DetalleFactura.objects.get(id=1)
det1.delete()
DetalleFactura.objects.filter(id=2).delete()
#------------------------------------------------------#
prod=Producto.objects.all()
prod=Producto.objects.get(id=2)
Producto.objects.filter(id__lte=2)
Producto.objects.exclude(descripcion__icontains='Cola')
Producto.objects.filter(id__gte=4)
Producto.objects.filter(id__gt=4).values('id','descripcion')
Producto.objects.filter(id__lt=4).values('id','descripcion')
Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')
#---------------------------------------------------------------------------------------------#
Factura.objects.filter(cliente__nombre='ginger luna')
cli= Cliente.objects.get(nombre='ginger luna')
cli.factura_set.all()
cli.factura_set.filter(id=2)
Factura.objects.select_related('cliente').filter(cliente__nombre='ginger luna')
Cliente.objects.prefetch_related('producto').filter(nombre='ginger luna').values('nombre','producto__descripcion')