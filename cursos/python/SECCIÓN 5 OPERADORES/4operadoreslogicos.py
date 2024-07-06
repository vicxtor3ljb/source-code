# Operadores lógicos (and, or, not)
numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8

numero1 > numero2
print(numero1 > numero2) 

numero3 < numero4
print(numero3 < numero4) 

#para que sea cierto tienen que ser ciertas las partes izquierda y derecha
(numero1 > numero2) and (numero3 < numero4)
print((numero1 > numero2) and (numero3 < numero4))

numero3 > numero4
print(numero3 > numero4)

(numero1 > numero2) and (numero3 > numero4)
print((numero1 > numero2) and (numero3 > numero4))

# el operador 'or', es para verificar que se de alguna de las dos condiciones, 
# si alguna opción es verdadera, el resultado es verdadero
(numero1 > numero2) or (numero3 > numero4)
print((numero1 > numero2) or (numero3 > numero4))

numero3 > numero4
print(numero3 > numero4)

# se usa el operador 'not' para evaluar lo contrario. 
not(numero3 > numero4)
print(not(numero3 > numero4))
