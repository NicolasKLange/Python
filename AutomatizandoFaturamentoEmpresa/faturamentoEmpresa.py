# Lendo o arquivo de texto com as vendas da loja
# Estrutra With, serve para abrir arquivos em Python

# Dentro do ()  passar o nome do arquivo e como quer abrir o arquivo
# r = read -> Ler o arquivo
# w = write -> Escrever no arquivo

# A variável arquivo são as informações que estão no arquivo
with open("vendasLoja.txt", "r") as arquivo:
    # lendo o arquivo e armazenando o texto na variavel texto
    texto = arquivo.read()
# split -> Separa o texto em vários itens
# neste caso separa o texto em linhas pelo enter
# Vira uma lista de valores onde cada item é uma linha
lista_texto = (texto.split("\n"))


# Inicializando o faturamento com o valor 0
faturamento = 0

# Excluir a primeira linha, pois não tem valor para somar
# [1:] -> faz com que pegue o primeiro índice até o último
# lembrando que começa no índice 0 por isso coloca 1
lista_texto = lista_texto[1:]

# Para cada linha do arquivo,
for linha in lista_texto:
    # Descobrindo a posição do ; de cada linha
    # find -> procura ;
    posicao_pv = linha.find(";")
    # O valor que irá somar, que é o valor depois do ;
    # ou seja, na linha é a posição do ; mais 1
    # Float -> Transforma String em numero decimal
    # .strip() - > Remove espaços em branco ou \n extras.
    valor_string = linha[posicao_pv+1:].strip()

    # Try Catch, verifica se tem algum valor inválido
    try:
        valor = float(valor_string)
        # Somando valor de cada linha no faturamento total
        faturamento += valor
    # Se achar algum valor errado mostra-o
    # f -> Usado para colocar as variaveis mais facil,
    # colcandoas varaiveis dedntro de {} no texto
    except ValueError:
        print(f"Valor inválido na linha: {linha}")

# Exibindo valor do faturamento
print(f"Faturamento: {faturamento}")
# cd "C:\Users\Nicolas Lange\Documents\Python\AutomatizandoFaturamentoEmpresa"
# python faturamentoEmpresa.py
