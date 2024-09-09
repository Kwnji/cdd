hora1 = int(input("Digite a hora:"))
minuto1 = int(input("Digite os minutos:"))
hora2 = int(input("Digite a hora:"))
minuto2 = int(input("Digite os minutos:"))

horatotal= hora1+hora2
horapar=horatotal%12
horaadd=horapar+1

min=minuto1+minuto2
mintotal= min%60

if min>60:
    print(f'{horaadd}:0{mintotal}')
else:
    print(f"{horapar}:0{mintotal}")
