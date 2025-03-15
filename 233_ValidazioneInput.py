def ottieniNumero():
    while True:
        try:
            numero = int(input("Inserisci un numero: "))
            return numero
        except ValueError:
            print("Devi inserire un numero intero!")


print(ottieniNumero())