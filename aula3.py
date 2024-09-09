n1 = float (input ("Digite sua primeira nota:"))
n2 = float (input ("Digite sua segunda nota:"))
n3 = float (input ("Digite sua terceira nota:"))
calculo = (n1 +n2+n3) / 3

if calculo >= 4:
    print ("vc está na recuperação")
else:
    if calculo >= 7:
        print ("vc está aprovado")
    else:
        print ("vc n está aprovado")