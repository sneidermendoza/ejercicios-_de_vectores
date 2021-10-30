# Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
# realice la productoria y en la segunda la sumatoria. Entregue los valores
# resultantes

list = []
summation = 0
productive = 1

while True: 
    length = int(input("Ingrese cuantos elementos va a tener la lista, recuerde que el tamaño de la lista tiene que ser par: \n"))
    if length % 2 != 0:
        print("Numero impar, ingrese un nuevo numero")
    else:
        break 

for i in range(length):
    number = int(input("Ingrese un numero para agregar a la lista: \n"))
    list.append(number)

print(list)

print("////////////////////////////////////////////////////////////////////")

div = int(length / 2)

for i in range(div):
    productive *= list[i]
print(productive)


for i in range(div,len(list)):
    summation += list[i]
print(summation)


