# la cadena de caracteres se refiere a una seria de datos que ocupan una serie 
#Ejemplo A,1,?;JM= Y SI SE UNE forma cadena de caracteres 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print("hola mundo")
print("KAROL DAYANA HERRERA PAEZ")
curso ="programacion uno"
print ("su curso es:",curso)
institucion = "SENA" #variable tipo texto
trimestre = "1" #variable tipo numero
#imprimir varias variables
print("su curso es:",curso,"su institucion es:", institucion,"su trimestre es:", trimestre)
print(len(institucion)) #el comando len sirve para contar los numeros de caracteres
universidad = "SENA"
print(len(curso))
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(curso.upper()) #el comando uper sirve para poner el la cadena en MAYUSCULA
print(curso.lower()) #el comando lower sirve paraponer la cadena en minuscula
print(institucion[0]) #los corchetes sirven para traer la pisicion de la cadena 
print(institucion[1])
print(institucion[2])
print(institucion[3])
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(institucion[0:4]) #los corchetes y los dos puntos trae un rango de la cadena

#CONCATENAR 
print(institucion + "  " +curso.upper())
#COMPARAR UNA CADENA
print(curso == institucion)
print(institucion == "SENA")
print("Analisis y desarrollo en sistemas".replace("sistemas", "software"))
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
nombre = "Karol Dayana Herrera Paez"
correo =f"{nombre[0:1]}{nombre[6:7]}{nombre[13:20]}{nombre[21:22]}@sena.edu.co".lower()
print(correo)
print("su correo es", correo)