def filtraPari(lista):
    pari = [i for i in lista if i % 2 == 0]
    return pari

lista = [1, 5, 7, 8, 9, 10, 12, 15, 18, 20]
print(filtraPari(lista))