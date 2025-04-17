# Mostrar uma lista de carros
print("**** Lista de Carros ****")
lista_carros = ["Camaro", "Porsche GT3", "Lamborguini"]

for carro in lista_carros:
    print(carro)


# Mostrar uma lista de nomes com a primeira letra maiúscula
print("\n**** Lista de Nomes ****")
lista_nomes = ["nicolas", "carlos", "roberta"]

for nome in lista_nomes:
    # Capitalize = deixar primeira letra maiúscula
    print(nome.capitalize())


# Mostrar o preço com devido imposto aplicado de 10%
print("\n**** Lista de Preços com Impostos(10%) ****")
lista_precos = [20, 10, 40, 50, 45]

for preco in lista_precos:
    imposto = preco * 0.1
    print("Original: ", preco, " I Com Imposto: ", (preco + imposto))
