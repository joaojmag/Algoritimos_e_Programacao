#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

somaIdade = 0
acimade90 = 0
for i in range(4):
    idade = int(input())
    peso = float(input())
    somaIdade += idade
    if peso > 90:
        acimade90 = acimade90 + 1
mediaidade = somaIdade / 4
print("Qtd pessoas > 90 Kg: %i" % acimade90)
print("Idade média: %.2f" % mediaidade)