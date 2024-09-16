opcao = 1
while opcao !=2:
    num = 0
    med = 0
    alunos = int (input ("Digite um numero"))
    while num < alunos:
        notas = float (input ("Digite a nota do aluno:"))
        med += notas
        num = num + 1
    total = med/alunos
    print (f"A media dos alunos sao {total} ")
    opcao = int (input (f"Deseja continuar \n"
                        "1 - para continuar\n"
                        "2 - para sair"))


