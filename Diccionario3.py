productos = { 
'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}, 
'Chocorramo':{'costo':700, 'precio':1000, 'cantidadDisponible':12}
}

for producto,info in productos.items():
    #info = productos[producto]
    gananciaUnitaria = info.get("precio")-info.get("costo")
    gananciaTotal = gananciaUnitaria*info.get("cantidadDisponible")
    print("Ganacia del producto:"+producto+" es de "+str(gananciaTotal))