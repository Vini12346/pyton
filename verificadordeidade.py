ano = 2025
ano_nasc = int(input("Digite o ano do seu nascimento: "))
idade = ano - ano_nasc
print("Idade em ",ano," é ", idade)
if idade == 16:
    print("Pode votar!")
else:
    print("Não pode votar!")
 