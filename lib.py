#biblioteca com as funçoes matematicas
import math
def tabuada(valor):
    for cont in range(0, 11):
        print(f'{cont} X {valor} = {cont * valor}')


def fatorial(valor):
    #for cont in range(1, valor+1):
    if valor > 1:
        fat = valor * fatorial(valor - 1)
        return fat
    else:
        return 1


#print(f'\n{5}! = {fatorial(5)}\n')
