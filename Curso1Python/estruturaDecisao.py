nota = float(input("Informe a nota: "))

frequencia = int(input("Informe a sua frequência: "))

# Estrutura de decisão, verificar se esta aprovado ou reprovado
# de acordo com a nota e frequencia

if (nota >= 6.0 and frequencia >= 70):
    print("Você está aprovado!!")
elif (nota >= 6.0 and frequencia < 70):
    print("Você está reprovado por frequência.")
elif (nota < 6.0 and frequencia >= 70):
    print("Você está reprovado por nota.")
else:
    print("Você está reprovado.")
