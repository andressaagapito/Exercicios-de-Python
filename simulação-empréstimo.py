print ('#'*30)
print ("    Simule seu empréstimo!")
print ("-"*45)
casa = float(input("     Qual o valor da casa? R$"))
salario = float(input("     Qual o salário do comprador? R$"))
anos = int(input("     Quantos anos de financiamento? "))
prestação = casa / (anos*12)
minimo = salario * 30/100
print("Para pagar uma casa de R${:.3f} em {} anos".format(casa, anos), end='')
print ('a prestação será de R${:.2f}.'.format(prestação))
if prestação <= minimo:
    print ("Empréstimo será concedido.")
else:
    print ("Emprestimo negado!")