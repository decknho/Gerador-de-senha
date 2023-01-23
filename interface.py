def senhas():
    from caracteres import caractere
    from random import randint
    quantidade = int(input('Quantas senhas você quer?\n-> '))
    tamanho = int(input('Quantos caracteres você quer para sua senhas?\n-> '))
    print('-' * 45)
    print()
    cont = 1
    print('-=' * 5, 'Senhas geradas', '=-' * 5)
    while quantidade != 0:
        print(f'{cont}° senha -> ', end='')
        cont += 1
        for c in range(0, tamanho):
            print(f'\033[34m{caractere[randint(0, 72)]}', end='')
        print('\033[m')
        quantidade -= 1
    print('-=' * 18)
    print()