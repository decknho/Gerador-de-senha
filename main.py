from interface import senhas
while True:
    print('\033[34m')
    print('-' * 27)
    print('[ 1 ] - Gerar senhas\n'
          '[ 2 ] - Finalizar programa')
    print('-' * 27)
    print('\033[m')
    print('-' * 27)
    print('-=\033[31m Só aceita os n° 1 e 2 \033[m=-')
    escolha = 0
    while escolha != 1 and escolha != 2:
        escolha = int(input('O que você deseja fazer?\n-> '))
    if escolha == 1:
        senhas()
    if escolha == 2:
        print('-' * 27)
        print('\033[31m')
        print('-' * 27)
        print(f'{"Programa finalizado":^27}')
        print('-' * 27)
        print('\033[m')
        break
