# recebe o grau da equação
grau = int(input('Digite o grau da equação: '))

# verifica se o grau é válido
if grau < 1 or grau > 2:
    print("Grau inválido")

# grau 1
else:
    if grau == 1:
        print("A equação é do primeiro grau")
        a = int(input("Digite o valor de a: "))
        if a == 0:
            print('Valor de a inválido')
        else:
            b = int(input("Digite o valor de b: "))
            x = -b / a
            print(f"{x:.2f}")
        
    if grau == 2:
        print("A equação é do segundo grau")
        a = int(input("Digite o valor de a: "))
        if a == 0:
            print('Valor de a inválido')
        else:
            b = int(input("Digite o valor de b: "))
            c = int(input("Digite o valor de c: "))
            delta = (b**2)-(4*a*c)
            if delta < 0:
                print('A equação não possui raízes reais')
            elif delta == 0:
                print("A equação possui apenas uma raiz real")
                x = (-b+delta**0.5)/2*a
                print(f'X = {x:.2f}')
            elif delta > 0:
                x1 = (-b + delta**0.5)/2*a
                x2 = (-b - delta**0.5)/2*a
                print("A equação possui duas raízes reais")
                print(f"{x1:.2f}")
                print(f'{x2:.2f}')