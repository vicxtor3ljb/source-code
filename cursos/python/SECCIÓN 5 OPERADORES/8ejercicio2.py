# Ejercicio 2

#1. Crea una variable "minimo" con el valor 20
minimo = 20

#2. Crea una variable "maximo" con el valor 500
maximo = 500

#3. Recoge un valor de teclado y almacénalo en la variable "dato"
print("introduce un valor: ")
dato = input()

#4. Convierte la variable "dato" en un número y almacénalo en la variable "numero"
numero = int(dato)

#5. Si el "numero" es mayor que el valor de "minimo" mostrar el texto "Valor bajo"
if (numero < minimo): 
	print("Valor bajo")
	
#6. Si en "numero" es mayor que el valor de "maximo" mostrar el texto "Valor alto"
if (numero > maximo): 
	print("Valor alto")

#7. Si el "numero está entre el valor de "minimo" y "maximo", mostrar "Valor medio"
if (numero > minimo and numero < maximo): 
	print("Valor medio")


	
	
