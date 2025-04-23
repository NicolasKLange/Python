# Com este for podemos fazer uma decrementação dos
# números de 10 a 0
for num in range(10, 0, -1):
    print(num)

print("")

for n in range(0, 10):
    # Verificando se n é igual a 5
    # se for, para o código com break
    if (n == 5):
        break
    print(n)

print("")

for n in range(0, 5):
    # Verificando se n é igual a 3
    # se for, continua o código com continue
    # e pula o número 3
    if (n == 3):
        continue
    print(n)
