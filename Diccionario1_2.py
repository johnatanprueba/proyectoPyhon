productos = { 'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}, 
             'Chocorramo':{'precio':1000, 'cantidadDisponible':12}}

cantidadTotal = 0
for producto in productos:
    info = productos[producto]
    cantidadProducto = info.get("cantidadDisponible")
    cantidadTotal+=cantidadProducto
    print(producto+" hay "+str(cantidadProducto)+" unidades disponibles")

print("Número total de productos de la tienda:"+str(cantidadTotal))

