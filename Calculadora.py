import math

x1 = float(input("Digite o primeiro número (x1): "))

print("\n--- MENU DE OPERAÇÕES ---")
print("'s' -> Soma           | 'sin'  -> Seno")
print("'m' -> Multiplicação  | 'cos'  -> Cosseno")
print("'d' -> Divisão        | 'log'  -> Logaritmo (base e)")
print("'u' -> Subtração      | 'sqrt' -> Raiz Quadrada")
print("'p' -> Potência (x1^x2)")

opcao = input("\nEscolha a operação: ").lower()

# LÓGICA DE SELEÇÃO
if opcao == 's':
    x2 = float(input("Digite o segundo número (x2): "))
    resultado = x1 + x2
elif opcao == 'u':
    x2 = float(input("Digite o segundo número (x2): "))
    resultado = x1 - x2
elif opcao == 'm':
    x2 = float(input("Digite o segundo número (x2): "))
    resultado = x1 * x2
elif opcao == 'd':
    x2 = float(input("Digite o segundo número (x2): "))
    if x2 != 0:
        resultado = x1 / x2
    else:
        resultado = "Erro: Divisão por zero!"
elif opcao == 'p':
    x2 = float(input("Digite o expoente (x2): "))
    resultado = math.pow(x1, x2)
elif opcao == 'sin':
    resultado = math.sin(math.radians(x1))
elif opcao == 'cos':
    resultado = math.cos(math.radians(x1))
elif opcao == 'sqrt':
    if x1 >= 0:
        resultado = math.sqrt(x1)
    else:
        resultado = "Erro: Raiz de número negativo!"
elif opcao == 'log':
    if x1 > 0:
        resultado = math.log(x1)
    else:
        resultado = "Erro: Logaritmo de número <= 0!"
else:
    resultado = "Opção inválida!"

print(f"\nResultado final: {resultado}")