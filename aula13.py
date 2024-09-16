soma = 0
for x in range (1, 11):
    numero = int (input ("Digite um numero"))
    if numero % 2 != 0:
        soma += numero
        print (soma)
