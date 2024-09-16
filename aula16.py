valor=0
for x in range (10):
    val = int (input ("Digite um numero"))
    if val >= 10 and val <= 20:
        valor = valor + 1

print (f"Existem {valor} no intervalo de 10 á 20: {valor}\n"
       f"Valores fora do intervalo: {10 - valor}")


