from lib import fatorial, tabuada
while True:

    print('\n\t\t\t ------ Seja Bem Vindo ao nosso sistema Matematico ------ \n')

    print('1.Fatorial')
    print('2.Tabuada')
    print('3.Saida')

    op = int(input('Informe a opção desejada\n'))

    if op == 1:
        print('\n\tcalcula fatorial\n')

        num = int(input('Informe o numero\n'))

        fat = fatorial(num)

        print(f'{num}! = {fat}')

    elif op == 2:
        print('\n\tcalcula tabuada\n')

        num = int(input('Informe o numero\n'))

        tab = tabuada(num)

        print(f'Tabuada de {num} = {tab}')

    elif op == 3:
        print('Forte Abraço')
        break
