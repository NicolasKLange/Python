# Importando o módulo de estatisticas
import statistics as sta

valores = [10, 20, 30, 40, 50]

# Fazendo a media dos valores
mediaValores = sta.mean(valores)

# Fazendo a mediana dos valores
medianaValores = sta.median(valores)

print("Média", mediaValores)

print("Mediana", medianaValores)
