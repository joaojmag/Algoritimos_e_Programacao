#Lista modificada

#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

numero = int(input(""))

x = 1
y = 2

while y<=numero:
    x*=y
    y+= 1
   
print("%s! = %i"%(numero,x))