escolha = 1
while escolha != 2:
    nota1 = float (input("Digite sua 1 nota:"))
    while nota1<0 or nota1>10:
        nota1 = float(input("Digite sua 1 nota:"))

    nota2 = float (input("Digite sua 2 nota:"))
    while nota2<0 or nota2>10:
        nota2 = float(input("Digite sua 2 nota:"))

    media = (nota1+nota2)/2
    print (f"Sua foi de {media}")

    escolha = int(input("Digite 1 para continuar e 2 pra parar"))