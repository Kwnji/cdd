litros = float(input("Digite quantos litros:"))
combustivel = input("Qual tipo de combustivel?")

if combustivel == "G" or combustivel == "g":
    valor = litros * 5.8
    print(valor)
else:
    if combustivel == "E" or combustivel == "e":
        valor = litros * 4.9
        print(valor)
    else:
        print("Combustivel inválido")
