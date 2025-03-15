# parte 1
def saluta():
    print("Ciao, benvenuto!")

saluta()

# parte 2
def stampa_dettagli(nome, età):
    print(f"Nome: {nome}, Età: {età}")

stampa_dettagli("Marco", 25)

# parte 3
def somma(a, b):
    return a + b

risultato = somma(4, 6)
print(risultato)

# parte 4
def quadrato(n):
    return n * n

def valore_medio_quadrato(n):
    return n * n / 2

def somma_quadrati(a, b):
    return quadrato(a) + quadrato(b)

def calcola_media_somma_quadrati(a, b):
    return somma_quadrati(a, b) / 2

print(somma_quadrati(3, 4))

print(calcola_media_somma_quadrati(3, 4))
print(valore_medio_quadrato(3))
print(valore_medio_quadrato(4))