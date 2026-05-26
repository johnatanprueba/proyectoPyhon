librosDisponibles = [('El Perfume', 'Suskind', 'Misterio'),
                    ('La Metamorfosis', 'Kafka', 'Novela'), 
                    ('Misery', 'Stephen King', 'Misterio'), 
                    ('Harry Potter', 'J.K. Rowling', 'Novela'), 
                    ('El Principito', 'Saint-Exupery', 'Infantil'), 
                    ('El Codigo Da Vinci', 'Dan Brown', 'Misterio')] 

librosDisponiblesCopy = []
for tupla in librosDisponibles:
    tuplaAux = (tupla[0],tupla[2],tupla[1])
    librosDisponiblesCopy.append(tuplaAux)

print(librosDisponiblesCopy)