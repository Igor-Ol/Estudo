x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if (x + y > z) and (x + z > y) and (y + z > x):

    if x == y == z:
        print("Equilátero")
    elif x != y and y != z and x != z:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é um triângulo")
