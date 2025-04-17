salario = float(input("Informe o seu salário: "))

if salario <= 2000:
    print(salario, " = Estagiário")
elif salario > 2000 and salario <= 4000:
    print(salario, " = Programador Júnior")
elif salario > 4000 and salario <= 6000:
    print(salario, " = Programador Pleno")
else:
    print(salario, " = Programador Sênior")
