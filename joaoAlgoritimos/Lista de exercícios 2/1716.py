#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input()
salario = float(input())

if plano == "A":
    aumento = salario * 0.1
elif plano =="B":
    aumento = salario * 0.15
else:
    aumento = salario * 0.20
    
novoSal = salario + aumento
    
print("Novo salário: R$%.2f" %(novoSal))
    
    
