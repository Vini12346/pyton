nota1 = float(input("Digite a nota da prova: "))
nota2 = float(input("Digite a nota do trabalho: "))
nota3 = float(input("Digite a nota da presença: "))
media = (nota1 + nota2 + nota3)/3
print("Média ", media)

if media >= 9:
    print("PD")
elif media >= 7:
    print("D")
elif media >= 3:
    print("ND")
else:
    print("ED")
