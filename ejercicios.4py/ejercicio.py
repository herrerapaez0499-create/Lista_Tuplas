# -------------------------------####
# OPERADORES ARITMÉTICOS
# -------------------------------####

#2. Promedio: Solicita tres números e imprime el promedio.
num1 = 75
num2 = 23
num3 = 15

promedio = (num1 + num2 + num3) / 3
print(" El promedio es:", promedio)

# 4. Módulo: Pide dos números y muestra el residuo de su división.
a = 456
b = 789

residuo = a % b
print(" El residuo de la división es:", residuo)

#####-------------------------------#####
# OPERADORES RELACIONALES###
####-------------------------------#####

# 6. Comparación: Solicita dos números y determina si son iguales, mayores o menores entre sí.
x = 10
y = 5
print("x es igual a y:", x == y)
print("x es mayor que y:", x > y)
print("x es menor que y:", x < y)

# 8. Nota aprobatoria: Ingresa una calificación y verifica si es mayor o igual a 3.0.
nota = 3.5
print("La nota es aprobatoria (>= 3.0):", nota >= 3.0)

# 10. Número par o impar: Usa operadores relacionales y módulo para determinar si un número es par o impar.
numero = 8
print("Número par:", numero % 3 == 0)


# -------------------------------####
# OPERADORES LÓGICOS
# -------------------------------####

# 12. Rango de edad: Verifica si una persona tiene entre 18 y 30 años (inclusive).
edad = 22
print("Está entre 18 y 30 años:", edad >= 18 and edad <= 30)

# 14. Negación: Pregunta si llueve y usa not para imprimir si NO está lloviendo.
llueve = False
print("¿NO está lloviendo?:", not llueve)


####-------------------------------####
# OPERADORES DE ASIGNACIÓN
####-------------------------------####

#16. Incremento: Declara una variable contador=0, incrementa en 1 cinconveces usando += e imprime el resultado.

contador = 0
contador += 1
contador += 1
contador += 1
contador += 1
contador += 1
print("\nValor final del contador es:", contador)

# 18. División acumulada: Empieza con un número 100 y divídelo entre 2tres veces usando /=.
numero = 100
numero /= 2
numero /= 2
numero /= 2
print("Resultado final de la división acumulada es:", numero)


####-------------------------------####
# OPERADORES BIT A BIT
####-------------------------------####

# 20. Desplazamiento: Dado un número, muestra el resultado al desplazar sus bits a la izquierda (&lt;&lt;) y a la derecha (&gt;&gt;) una posición.
num = 8
print("Número original:", num)
print("Desplazado a la izquierda (<< 4):", num << 6)
print("Desplazado a la derecha (>> 6):", num >> 2)






























