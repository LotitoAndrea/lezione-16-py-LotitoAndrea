import random

def filtraPari(lista):
    for i in lista:
        if i % 2 == 0:
            print(i, end=" ")

lista = [random.randint(1, 100) for i in range(10)]
print(lista)
print(filtraPari(lista))