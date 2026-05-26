productos = { 'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}, 
             'Chocorramo':{'precio':1000, 'cantidadDisponible':12}}

producto = input('¿Qué producto desea? ').title()
cantidad = int(input('¿Cuantos desea? '))

if producto in productos:
    infoPro = productos[producto]
    cantDispo = infoPro.get("cantidadDisponible")
    if(cantDispo<cantidad):
        print("No tenemos esa cantidad")
    else:
        cantDispo = cantDispo-cantidad
        infoPro["cantidadDisponible"] = cantDispo
else:
    print("Lo siento, el producto "+producto+" no está disponible")

print(productos)