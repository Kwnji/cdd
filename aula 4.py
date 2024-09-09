T1 = input ("Digite o nome do 1 time")
T2 = input ("Digite o nome do 2 time")

Gol1 = int (input ("Quantidade de gols"))
Gol2 = int (input ("Quantidade de gols"))

if Gol1 == Gol2:
    print ("empate")

else:
    if Gol1>Gol2:
        print ( "TIME 1 venceu")

    else:
        print ("time 2 venceu")