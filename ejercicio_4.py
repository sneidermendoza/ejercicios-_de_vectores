# De los n elementos de un vector dado identifique el número que mas se
# repite e indique cual es.

list = []

while True:
    elements = int(input("Por favor, ingrese un numero para agregar a la lista, ingrese 0 para cerrar lista: \n"))
    if elements != 0:
        list.append(elements)
    else:
        break

print(f"La lista es: {list}")

repeated = 0
more_repeated = [0]

for i in list:
    veces = list.count(i)
    if veces > repeated:
        more_repeated = i
        repeated = veces

print(f"El numero que mas se repite es: {more_repeated}")  
    
