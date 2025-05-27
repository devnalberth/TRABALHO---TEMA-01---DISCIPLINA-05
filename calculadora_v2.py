def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0."
    return a / b 

def calculadora(num1, num2, operacao):
    if operacao == "+" or operacao.lower() == "adicao":
        return adicao(num1, num2)
    elif operacao == "-" or operacao.lower() == "subtracao":
        return subtracao(num1, num2)
    elif operacao == "*" or operacao.lower() == "multiplicacao":
        return multiplicacao(num1, num2)
    elif operacao == "/" or operacao.lower() == "divisao":
        return divisao(num1, num2)
    else:
        return "Operação Inválida"
saida = ""

while saida.lower() != "n":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, / ou adição, subtração, multiplicação, divisão): ")

        resultado = calculadora(num1, num2, operacao)
        print("Resultado da operação:", resultado)
    except ValueError:
        print("Por favor, insira apenas números válidos.")

    saida = input("Deseja continuar? (S/N): ")