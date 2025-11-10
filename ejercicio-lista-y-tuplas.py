#Crea una lista con 5 productos de supermercado y muéstrala en pantalla.
print(" Lista de compras básica ")
lista_compras = ["Leche", "Huevos", "Arroz", "Pasta", "Pan"]
print(lista_compras)

#Tienes una lista con 4 comidas favoritas, cambia la segunda por un nuevo platillo.
comidas_favoritas = ["Pizza", "Hamburguesa", "Tacos", "Pasta"]
comidas_favoritas[1] = "Sushi"
print(comidas_favoritas)

#Crea una lista con 3 invitados a una fiesta, agrega dos más, y luego elimina uno.
invitados = ["Juan", "Maria", "Pedro"]
invitados.append("Lucia")
invitados.append("Ana")
invitados.remove("Pedro")
print(invitados)

#Crea una lista con 5 colores y muestra la lista en orden inverso usando reverse() o [::-1].
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Negro"]
colores.reverse()  
print(colores)

#Crea una lista con animales y usa len() para mostrar cuántos hay.
animales = ["Perro", "Gato", "Gallo", "Conejo", "Pato"]
print("Cantidad de animales:", len(animales))

#Crea una lista con elementos repetidos y usa set() para mostrar la lista sin duplicados.
elementos_repetidos = ["a", "b", "a", "c", "b", "d"]
sin_duplicados = set(elementos_repetidos)
print(sin_duplicados)

#Crea una lista de números y genera una nueva lista con el cuadrado de cada número usando un bucle o comprensión de listas.
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]
print(cuadrados)

#Une dos listas (por ejemplo, frutas y verduras) en una sola y muéstrala.
frutas = ["Manzana", "Banano"]
verduras = ["Tomate", "Lechuga"]
lista_combinada = frutas + verduras
print(lista_combinada)

#De una lista de números, elimina todos los que sean menores a 5.
numeros2 = [1, 3, 5, 7, 2, 8, 4]
numeros_filtrados = [n for n in numeros2 if n >= 5]
print(numeros_filtrados)

#Crea una lista que represente el inventario de una tienda. Permite que el usuario agregue y quite productos mediante input().
# Inventario de una tienda (VERSIÓN PARA PRINCIPIANTES)

# Inventario de una tienda (SIN input, todo automático)

inventario = []  # lista vacía

# Agregar productos automáticamente
inventario.append("Leche")
inventario.append("Pan")
inventario.append("Huevos")

print("Inventario después de agregar productos")
print(inventario)

# Eliminar un producto automáticamente
inventario.remove("Pan")

print("Inventario después de eliminar un producto")
print(inventario)




#Crea una tupla que represente la ubicación (x, y) de un punto y muéstrala.
coordenadas = (10, 20)
print(coordenadas)

#Crea una tupla con nombre, edad y ciudad, y muestra cada elemento con su etiqueta.
persona = ("Karol", 25, "Bogotá")
print("Nombre:", persona[0])
print("Edad:", persona[1])
print("Ciudad:", persona[2])

#Crea una tupla con 3 frutas y asígnalas a tres variables diferentes.
frutas = ("Manzana", "Banano", "Uva")
a, b, c = frutas
print(a, b, c)

#Intenta modificar una tupla y explica por qué da error.
tupla_no_modificable = (1, 2, 3)
# tupla_no_modificable[0] = 10  # Esto da error porque las tuplas NO se pueden modificar

#Crea dos tuplas y únelas en una sola.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_unida = tupla1 + tupla2
print(tupla_unida)

#Crea una tupla pequeña y repítela 3 veces usando el operador *.
tupla_repetida = (1, 2) * 3
print(tupla_repetida)

#Crea una tupla de números y encuentra el valor mayor y menor usando max() y min().
numeros_tupla = (5, 8, 2, 10, 3)
print("Máximo:", max(numeros_tupla))
print("Mínimo:", min(numeros_tupla))

#Crea una lista y conviértela a tupla con tuple().
lista_ejemplo = [10, 20, 30]
tupla_convertida = tuple(lista_ejemplo)
print(tupla_convertida)

#Crea una tupla y verifica si un elemento está en ella usando in.
colores = ("Rojo", "Verde", "Azul")
print("Verde está en la tupla:", "Verde" in colores)

#Crea una tupla y encuentra la posición de un elemento con .index().
tupla_nombres = ("Ana", "Luis", "Sofia", "Carlos")
print("Índice de Sofia:", tupla_nombres.index("Sofia"))

