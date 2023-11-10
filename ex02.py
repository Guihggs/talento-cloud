def calculadora_interativa():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Escolha a operação (0-4): "))

        if operacao == 0:
            print("Saindo da calculadora. Até logo!")
            break
        elif operacao in [1, 2, 3, 4]:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if operacao == 1:
                resultado = numero1 + numero2
            elif operacao == 2:
                resultado = numero1 - numero2
            elif operacao == 3:
                resultado = numero1 * numero2
            elif operacao == 4:
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    print("Erro: Divisão por zero. Tente novamente.")
                    continue

            print("Resultado:", resultado)
        else:
            print("Essa opção não existe. Tente novamente.")
            continue

if __name__ == "__main__":
    calculadora_interativa()
