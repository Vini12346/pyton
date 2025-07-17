import random

numero_secreto = random.randint(1, 10)

palpite = int(input("digite um palpite: "))

if(palpite == numero_secreto):

    print("você acertou")

else:

    print("tente outra vez")

    print("o numero secreto é: ", numero_secreto)

 