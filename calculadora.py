# calculadora.py

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

def main():
    print("Calculadora simples")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: por favor, digite números válidos.")
        return

    print(f"Soma: {soma(num1, num2)}")
    print(f"Subtração: {subtracao(num1, num2)}")
    print(f"Multiplicação: {multiplicacao(num1, num2)}")
    print(f"Divisão: {divisao(num1, num2)}")

if __name__ == "__main__":
    main()
