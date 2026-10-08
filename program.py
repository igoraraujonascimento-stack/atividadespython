#----ADIVINHE O NÚMERO----#
import random

numero_secreto = random.mandint(1, 20)
tentativas = 0

print('Pensei em um número de 1 a 20. Consegue acertar?')

while True:
    palpite = int(input("Seu palpite:"))
    tentativas += 1

    if palpite < numero_secreto:
        print('Muito baixo! Tente um número maior')
    elif paplpite > numero_secreto:
        print('Muito alto! Tente um número maior')
    else:
        print('Acertou em {tentativas} tentativa(s)!')
        break
else:
    print(f'Acabarqm')