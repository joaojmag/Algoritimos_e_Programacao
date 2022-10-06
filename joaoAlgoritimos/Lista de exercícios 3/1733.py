#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input("")
horas = float(input(""))

salario = 1192.40
hextra = 10
salario_extra = horas * hextra
bruto = (3 * salario) + salario_extra

print("Nome: %s"%nome)
print("Salário bruto: R$%.2f"%bruto)

if(bruto>2000) and (bruto>2000):
    desconto = bruto -(bruto*32/100)
    print("Salário líquido: R$%.2f" %desconto)

elif bruto <2400:
    desconto = bruto - (bruto *0.33)
    print("Salário líquido: R$%.2f" %desconto)