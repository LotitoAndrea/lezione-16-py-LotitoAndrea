def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)

print(fattoriale(5))
print(fattoriale(6))
print(fattoriale(7))
print(fattoriale(8))
print(fattoriale(0))
