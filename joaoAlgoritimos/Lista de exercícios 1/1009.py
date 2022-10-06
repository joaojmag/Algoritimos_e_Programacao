# https://www.beecrowd.com.br/judge/pt/problems/view/1009

A = str(input())
B = float(input())
C = float(input())

comissao = C * 0.15
salario = B + comissao

print("TOTAL = R$ %.2f" %(salario))
