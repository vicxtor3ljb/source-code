# Operadores de pertenencia (in, not in)
# Permiten verificar si un valor está dentro de una lista de valores o un objeto está dentro de una lista de objetos

# frutas1 es una lista de variables mientras frutas2 es una variable que representa una cadena de texto con la palabra "pera"

frutas1 = ["manzana","pera","naranja"]
frutas2 = "pera"
frutas3 = "melocotón"

# Si queremos verificar si "pera" está dentro de esta lista, este caso es muy sencillo, si la lista fuera muy grande y queremos verificar que el valor está dentro de esta lista, pues 
# utilizaríamos el valor de pertencia "in"

frutas2 in frutas1
print(frutas2 in frutas1)

# El operador "not in" es lo contrario a "in"
frutas2 not in frutas1
print(frutas2 not in frutas1)

frutas3 not in frutas1 
print(frutas3 not in frutas1)



