[14:42, 14/04/2023] +55 85 8816-0458: from symtable import *
print("Digite o grau da função")
N = int(input("> "))
if N < 1 or N > 2:
    print("Grau inválido")

if N ==1:
    print("A equação é do primeiro grau")
    a = int(input("Digite o número a:"))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = int(input("Digite o número b:"))
        x = Symbol
        x = -b / a
        a*x+b==0
        if -b % a !=0:
            print("x é igual a",-b,"/",a)
        if -b % a ==0:
            print("x é igual a {}".format(x))

if N ==2:
    print("A equação é do segundo grau")
    a = int(input("Digite o número a:"))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = int(input("Digite o número b:"))
        c = int(input("Digite o número c:"))
    …
[15:20, 18/04/2023] +55 85 8816-0458: print("Quantos primos?")
F = int(input("> "))
O = F
N = 2
i = 1
Lista = []
if F <=0:
    print("Insira um número maior")
if F > 0:
    while True:
        i = i + 1
        if N % i !=0:
            i = i + 1
        if N % i ==0 and i !=N:
            N = N + 1
            i = 1
        if N % i ==0 and i ==N:
            F = F - 1
            i = 1
            Lista.append(N)
            if F > 0:
                N = N + 1
            if F <=0:
                F = O
                print((F),Lista)
                break
