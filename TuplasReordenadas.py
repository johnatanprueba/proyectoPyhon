librosDisponibles = [('El Perfume', 'Suskind', 'Misterio'),
                    ('La Metamorfosis', 'Kafka', 'Novela'), 
                    ('Misery', 'Stephen King', 'Misterio'), 
                    ('Harry Potter', 'J.K. Rowling', 'Novela'), 
                    ('El Principito', 'Saint-Exupery', 'Infantil'), 
                    ('El Codigo Da Vinci', 'Dan Brown', 'Misterio')] 

def ordenar(tupla):
    return len(tupla[0])

librosDisponibles.sort(key=ordenar)

print(librosDisponibles)
