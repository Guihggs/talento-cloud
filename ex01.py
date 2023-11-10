def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        # Verifica se o divisor não é zero para evitar divisão por zero
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return 0
    else:
        print("Operação inválida. Escolha 1 para Soma, 2 para Subtração, 3 para Multiplicação, ou 4 para Divisão.")
        return 0

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1 para Soma, 2 para Subtração, 3 para Multiplicação, 4 para Divisão): "))

resultado = calculadora(numero1, numero2, operacao)
print("Resultado:", resultado)
