# Operadores de identidad (is, is not)
# Intentan identificar si dos objetos son realmente el mismo objeto
# o si son diferentes objetos


# frutas1 es una variable con una lista de dos elementos

frutas1 = ["manzana","pera"]

frutas2 = ["manzana","pera"]

frutas3 = frutas1

frutas3 is frutas1 
print(frutas3 is frutas1)

frutas3.append("naranja")
print(frutas3)

frutas1
print(frutas1)

#frutas3 y frutas1 comparten el mismo objeto con nombres de variables distintos

#el 'is not' es lo contrario al 'is'
frutas3 is frutas1
print(frutas3 is frutas1)

frutas3 is not frutas1
print(frutas3 is not frutas1)

