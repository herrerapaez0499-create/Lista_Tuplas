#LISTAS EN PYTHON
#Las listas son datos que tienen como caracteristicas ser mutables
#Las listas son ordenadas
#LAS LISTAS SE DEFINEN CON LLAVES
#Ejemplo
estudiante = ["ERIK","ZULETA","ANGIE","KAROL","LEONARDO"]
print(estudiante) #imprimir la lista
print(len(estudiante)) #Imprimir la cantidad de datos de la lista
print(estudiante[2]) #imprimir la posicion de la lista
estudiante[2] = "LORENA" #modificar o mutar una lista
print(estudiante) #Imprimir la lista nuevamente 
estudiante.append("DIEGO") #append sirve para agregar un objeto a la lista
print(estudiante) # Imprimir lista
estudiante.remove("ERIK") #remove sirve para elimin
print(estudiante) #rimprimir
del estudiante [3] #del sirve para eliminar 
print(estudiante)
print("mostrar todas las frutas")
for estudiantes in estudiante: 
    print("-",estudiante)
#=====================================================
#========TUPLAS====================
#=================================================
#LAS TUPLAS SON ORDENADAS
#LAS TUPLAS NO SON MUTABLES
#LAS TUPLAS SE DEFINEN CON ()
#EJEMPLO
equipos = ("nacional","millonarios","santafe","junior","america","tolima")
print(equipos)
print("el esquipo es ", equipos [3]) #muestra la pisicion


