def masCaracteres(palabras):
    pos = 0
    for x in range(len(palabras)):
        if len(palabras[x]) > len(palabras[pos]):
            pos = x 
    return palabras[pos]

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio","Septiembre", "Diciembre"]
print("Palabra con mas caracteres:",masCaracteres(palabras))