# Dicionario de produtos com for
# Todo dicionario tem o seu rótulo e o seu valor
produtos = {
    "Leite": 10,
    "Arroz": 20,
    "Carne": 35,
    "Pao": 7,
    "Ovo": 20,
}

# Passar a chave(Rótulo) do dicioanario
for produto in produtos:
    # Exibindo nome do produto e  valor do produto
    print(produto, ":", produtos[produto])
