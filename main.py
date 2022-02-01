from random import randint


presente = [['add', ['adicionar'], 'added', 'added'],                 ['arise', ['erguer', 'levantar'], 'arose', 'arisen'],
            ['awake', ['acordar', 'despertar'], 'awoke', 'awoken'],   ['answer', ['responder'], 'answered', 'answered'],]
# 0 = palavra     1 = traduções     2 = passado     3 = particípio
passado = [[]]
participio = [[]]

CENTER = 20


def get_word(list, number, delete=True):
    try:
        print(list[number])
        return list[number]
    except:
        print('Algo deu errado. Tente novamente')
        return 0


while True:
    try:
        choice = int(input('0 - presente\n1 - passado\n2 - participio\n3 - Sair\n: '))
    except:
        print('ERRO: Tente novamente')
    
    # Sair
    if choice == 3:
        break
    #

    while True:
        # Verificar se o programa foi finalizado
        if len(presente) == 0:
            print('\033[32mParabéns! Você finalizou o programa.\033[m')
            break
        #
        
        if choice == 0: # Presente
            num = randint(0, len(presente) - 1)
            atual_list = presente[num]

            resp = str(input(f'O que significa {atual_list[0]}? ')).lower().strip()

            # Sair
            if resp == 'leave' or resp == 'sair':
                break
            #
            
            # Acertou?
            if resp in atual_list[1]:
                print('\033[32mCorreto ✅\033[m')
                del(presente[num])
            else:
                print('\033[31mErrado ❌\033[m')
            #

            print()

            # Coletando traduções
            trad = ''
            for c in  atual_list[1]:
                trad += f'{c} '
            #
            
            # Mostrando dados
            print(f'Presente:\033[34m{atual_list[0] :>20}\033[m')
            print(f'Passado:\033[34m{atual_list[2] :>20}\033[m')
            print(f'Participio:\033[34m{atual_list[3] :>20}\033[m')
            print(f'\nPossíveis traduções: \033[33m{trad}\033[m\n')
            #


        elif choice == 1:
            print()
        elif choice == 2:
            print()
        else:
            print()