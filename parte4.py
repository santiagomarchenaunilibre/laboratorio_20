def suma(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma
def mayor(lista):
    may = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may 
    
listadevalores = [12,3,6,78,45,21]
print("La lista compelta es: ", listadevalores)
print("La suma de todo los elemntos de la lista es: ",suma(listadevalores))
print("El numero mayor encontrado en la lista es: ",mayor(listadevalores))