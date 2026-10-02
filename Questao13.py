def particiona(lista, baixo, alto):
    pivo = lista[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1
def quicksort(lista, baixo=0, alto=None):
    if alto is None:
        alto = len(lista) - 1
    if baixo < alto:
        p = particiona(lista, baixo, alto)
        quicksort(lista, baixo, p - 1)
        quicksort(lista, p + 1, alto)
    return lista
print(quicksort([8, 3, 5, 1, 9, 2]))
print(quicksort([4, 7, 1]))