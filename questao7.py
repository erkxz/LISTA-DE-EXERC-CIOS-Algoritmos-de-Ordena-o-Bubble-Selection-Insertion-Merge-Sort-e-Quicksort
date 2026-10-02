def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
print(selection_sort([5, 2, 8, 1, 9]))
print(selection_sort([3, 1, 2]))