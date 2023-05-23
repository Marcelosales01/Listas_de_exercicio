numeros = []

for numero in range(1000, 2001):
    if numero % 11 == 5:
        numeros.append(numero)

print("Números entre 1.000 e 2.000 que divididos por 11 têm resto igual a 5:")
for numero in numeros:
    print(numero)