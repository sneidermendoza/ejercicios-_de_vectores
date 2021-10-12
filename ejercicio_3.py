# Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
# las siguientes operaciones:
# a. Suma
# b. Resta

vector_1 = []
vector_2= []
resultant_vector_sum = []
resultant_vector_subtraction = []
list = int(input("Digite el tamaño de las listas: \n"))

for i in range(0, list, 1):
    elements = int(input("Ingrese un elemento de la lista 1: "))
    vector_1.append (elements)

print("//////////////////////////////")

for i in range(0, list, 1):
    elements = int(input("Ingrese un elemento de la lista 2: "))
    vector_2.append (elements)

for i in range(0, list, 1):
    resultant_vector_sum.append (vector_1 [i] + vector_2 [i])

for i in range(0, list, 1):
    resultant_vector_subtraction.append (vector_1 [i] - vector_2 [i])

print(f"Lista 1: {vector_1}")
print(f"Lista 2: {vector_2}")
print(f"El resultado de la suma de las listas es: {resultant_vector_sum}")
print(f"El resultado de la resta de las listas es: {resultant_vector_subtraction}")
