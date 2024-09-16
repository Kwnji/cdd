alunos = int (input("Digite o numero:"))
soma = 0
for x in range (1, alunos+1):
    notas = int (input ("Digite a nota:"))
    soma = soma + notas
media = soma/ alunos
print(f"{media}")