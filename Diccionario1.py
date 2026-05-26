productos = { 'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}, 
             'Chocorramo':{'precio':1000, 'cantidadDisponible':12}}

producto = input('¿Qué producto desea? ').title()
cantidad = int(input('¿Cuantos desea? '))

if producto in productos:
    infor  = productos[producto]
    precioProducto = infor.get("precio")   
    precioTotal = cantidad*precioProducto
    print("El precio total es de $"+str(precioTotal))
else:
    print("Lo siento, el producto "+producto+" no está disponible")




    

