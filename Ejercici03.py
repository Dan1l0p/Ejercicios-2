def modificar(lista):

    lista = list(set(lista))
    lista.sort(reverse=True)
    
    lista2 = []
    for num in lista:
        if num % 2 == 0:
            lista2.append(num)
        else:
            pass
    suma = sum(lista2)
    lista2.insert(0,suma)
    return lista2
    



lista = [1,2,3,4,5,5,2,8,9,2,]
newlista= modificar(lista)
print(modificar(lista))
print(newlista[0]== sum(newlista[1:]))
