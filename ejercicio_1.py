# De los n elementos de un vector dado calcule:
# a. La sumatoria
# b. La productoria
# c. El Mayor Elemento
# d. El menor Elemento

list = [] 
major_element = 0
minor_element = 0 
sumatoria = 0
productoria = 1
elements = int(input("Por favor, ingrese un numero para agregar a la lista, ingrese 0 para cerrar lista: \n"))

while elements != 0:
    list.append (elements)
    elements = int(input("Por favor, ingrese un numero para agregar a la lista, ingrese 0 para cerrar lista: \n"))

for i in list:
    major_element = max(list)
    minor_element = min(list)
    sumatoria += i
    productoria *= i


    
print( list)
print(f"la sumatoria es: {sumatoria}")
print(f"la productoria es:{productoria}")
print(f"El mayor elemento de la lista es: {major_element}")
print(f"El menor elemento de la lista es: {minor_element}")