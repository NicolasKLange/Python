# Lista de numeros inteiros
listaNumeros = [1, 2, 3, 4, 5]

# Mostra o tamanho da lista
print("Tamanho da lista: ", len(listaNumeros))

# Lista com diferentes tipos de dados
listaDiferente = [1, 2, 3, "Nicolas", True]

print(listaDiferente)

# Lista com range
listaRange = list(range(0, 10))

print(listaRange)

# Modificar elemento do indice
listaNumeros[0] = 10
print(listaNumeros)

# Laço para percorrer elementos da lista e  imprimir um por um
for num in range(0, len(listaRange)):
    print(listaRange[num])
