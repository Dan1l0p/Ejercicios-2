def modificar(lista):
    nueva_lista = []
    nueva_lista = set(lista)
    for num in lista:
        if not num % 2 == 0:
                nueva_lista.remove(num)
        else:
                nueva_lista.append(num)

        return nueva_lista

    lista_inver = nueva_lista.sort(reverse=True)
    return nueva_lista
    



lista = [1,2,3,4,5,5,4,8,9,2,]
nueva_lista= modificar(lista)
print(modificar(lista))
print(lista)
