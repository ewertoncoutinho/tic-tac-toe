import random
import re


def instruction():
    print('Escolha a casa de acordo com a numeração descrita abaixo:')
    print('           ')
    print(' 1 | 2 | 3 ')
    print(' 4 | 5 | 6 ')
    print(' 7 | 8 | 9 ')
    print('___________')


def lineBreak():
    print('')
    print('')


def imprime_casas(casas):
    for i in range(len(casas)):
        print(casas[i], end='  ')
        if i == 2 or i == 5:
            print('')


instruction()
casas = ["_"] * 9
regex = '^(?:X..X..X..|.X..X..X.|..X..X..X|XXX......|...XXX...|......XXX|X...X...X|..X.X.X..)$'
i = 0
while i <= 4:
    lineBreak()
    x = int(input('Faça sua escolha: '))
    while casas[x - 1] != '_':
        print('Escolha inválida')
        imprime_casas(casas)
        lineBreak()
        x = int(input('Faça sua escolha: '))
    casas[x - 1] = 'X'
    if i < 4:
        CPU = random.randint(1, 9)
        while casas[CPU - 1] != '_':
            CPU = random.randint(1, 9)
        casas[CPU - 1] = 'O'
    imprime_casas(casas)
    result = ''.join(map(str, casas))
    i += 1
    if re.match(regex, result):
        lineBreak()
        print("Você venceu, parabéns!")
        print("Resultado:")
        imprime_casas(casas)
        break
    else:
        lineBreak()
        print("Resultado:")
        imprime_casas(casas)
