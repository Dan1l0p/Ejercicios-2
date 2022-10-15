def modificar(lista):

    nueva_lista = list(set(lista))
    nueva_lista.sort(reverse=True)
    
    nueva_lista2 = nueva_lista
    for num in lista:
        if not num % 2 == 0:
            nueva_lista2.pop(num)
        else:
            nueva_lista2.append(num)
    suma = sum(nueva_lista2)
    nueva_lista2.insert(0,suma)
    return nueva_lista2
    



lista = [1,2,3,4,5,5,4,8,9,2,]
nuevalista= modificar(lista)
print(modificar(lista))
print(nuevalista[0]== sum(nuevalista[1:]))
