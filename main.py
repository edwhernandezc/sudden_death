# Primer punto

def firtslist(list):  # Primero declaramos una función condicional
    for element in list:
        if list.index(element) == 0:
            return element


numeros = [['a', 'b', 'c'], [1, 2, 3]]

list(filter(firtslist, numeros))


# Fin primer punto

# Tercer punto y cuarto
def carga_lista():
    li = []
    for x in range(5):
        valor = int(input("Ingrese valor:"))
        li.append(valor)
    return li


def retornar_mayormenor(li):
    ma = li[0]
    me = li[0]
    for x in range(1, len(li)):
        if li[x] > ma:
            ma = li[x]
        else:
            if li[x] < me:
                me = li[x]
    return [ma, me]


lista = carga_lista()
rango = retornar_mayormenor(lista)
print("Mayor elemento de la lista:", rango[0])
print("Mayor elemento de la lista:", rango[1])
# Fin tercer y cuarto punto


# Sexto punto
list = []


def triangular(x, y):
    ty = y(y + 1) / 2
    if ty == x:
        return list.append(x)

def sumList(list):
    sum = 0
    for element in list:
        sum = element + sum
    return sum

# final sexto punto