def firtslist(list):  # Primero declaramos una función condicional
    for element in list:
        if list.index(element) == 0:
            return element


numeros = [['a', 'b', 'c'], [1, 2, 3]]

list(filter(firtslist, numeros))
