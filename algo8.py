pin = 1234
senha = int(input("Digite sua senha:"))
tentativas = 1
while senha != pin and tentativas < 3:
    senha = int(input("Senha incorreta, digite novamente"
                      f"voce tem {3 - tentativas}"))
    tentativas += 1
if tentativas == 3 and senha != pin:
    print("Senha bloqueada")
else:
    print("login efetuado com sucesso")
