from time import sleep
print ("#"*20, end='')
print (" \033[1m Calculadora \033[m ", end ='')
print ("#"*20)
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opção = 0
while opção != 5:
    print ("""
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA""")
    opção = int(input(" >>>>>>>  Escolha qual operação: "))
    if opção == 1:
        print (f"{n1} + {n2} = {n1+n2}")
    elif opção == 2:
        print (f"{n1} * {n2} = {n1*n2}")
    elif opção == 3:
        if n1 > n2:
            print("O primeiro valor é maior!")
        elif n1 < n2:
            print ("O segundo valor é maior!")
        elif n1 == n2:
            print ("Os dois valores são iguais!")
    elif opção == 4:
        print ("Informe os numeros novamente!")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opção == 5:
        print ("Finalizando...")
    else:
        print ("Opção inválida! Tente novamente!")
    print ("*"*10)
    sleep (1)
print ("Fim do programa!")
