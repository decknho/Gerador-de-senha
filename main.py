from interface import senhas
while True:
    print('[ 1 ] - Gerar senhas\n'
          '[ 2 ] - Finalizar programa')
    print('\033[31mSó aceita os n° 1 e 2...\033[m')
    escolha = 0
    while escolha != 1 and escolha != 2:
        escolha = int(input('O que você deseja fazer? '))
    if escolha == 1:
        senhas()
    if escolha == 2:
        print('Programa finalizado...')
        break
