# De los n elementos de un vector dado calcule:
# a. Cantidad de elementos pares
# b. Cantidad de elementos impares
# c. Cantidad de elementos primos

def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

list = []
even = 0
odd = 0
prime = 0

elements = int(input("Por favor, ingrese un numero para agregar a la lista, ingrese 0 para cerrar lista: \n"))

while elements != 0:
    list.append(elements)
    elements = int(input("Por favor, ingrese un numero para agregar a la lista, ingrese 0 para cerrar lista: \n")) 

print(f"Dentro de la lista {list} hay: ")
for i in list:
    if es_primo(i):
        prime += 1

    if i % 2 == 0:
        even +=1
    else:
        odd += 1

print(f"Hay {prime} numeros primos")
print(f"Hay {even} numeros pares")
print(f"Hay {odd} numeros impares")