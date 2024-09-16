# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
num1 = int(input("digite o 1° número: "))
num2 = int(input("digite o 2° número: "))
operaçao = input("qual a operação que você deseja executar? ")

# execução para cada operação.
if operaçao == "soma":
    print(f"{num1} + {num2} =", num1+num2)
elif operaçao == "subtração":
    print(f"{num1} - {num2} =", num1-num2)
elif operaçao == "multiplicação":
    print(f"{num1} * {num2} =", num1*num2)
elif operaçao == "divisão":
    print(f"{num1} / {num2} =", num1/num2)
    