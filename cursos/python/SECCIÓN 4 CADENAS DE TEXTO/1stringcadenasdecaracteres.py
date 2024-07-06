# 1 String (cadenas de caracteres) 

cadena = "Hola mundo"

print(cadena)

# H o l a   m u n d o
# 0 1 2 3 4 5 6 7 8 9


#   H   o  l  a     m  u   n  d   o
#  -10 -9 -8 -7 -6 -5 -4  -3 -2  -1

cadena[5]

print(cadena[5])

cadena[-1]
print(cadena[-1])

cadena[-10]
print(cadena[-10])

cadena[2:7]
print(cadena[2:7])

cadena[2:]
print(cadena[2:])

# error: cadena[5] = 'p'

cadena[5]
print(cadena[5])

cadena1 = "Hola"
cadena2 = "mundazo"
cadena3 = " "
cadenafinal = cadena1 + cadena3 + cadena2

print(cadenafinal)
