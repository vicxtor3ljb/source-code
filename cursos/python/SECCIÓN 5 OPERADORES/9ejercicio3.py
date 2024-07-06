# Ejercicio 3
# 1. Crear una variable "numeros" con la lista de los numeros del 1 al 10 (ambos incluidos)
numeros = [1,2,3,4,5,6,7,8,9,10]

# 2. Mostrar el valor de la variable "numeros"
print(numeros)

# Recoger un dato del teclado y almacenarlo en la variable "dato"
print("Escribe un numero: ")
dato = input()

# Convertir "dato" en numérico y almacenarlo en la variable "numero"
numero = int(dato)

# Si el valor de "numero" esta en la lista de números, mostrar el mensaje "Si"
if (numero in numeros):
	print("Si")

# Si el número introducido no está en la lista de números, mostrar el mensaje "No"
if (numero not in numeros):
	print("No")

