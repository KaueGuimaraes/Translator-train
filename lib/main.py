from random import randint

import lista


PRESENTE_DEF = lista.get()
presente = PRESENTE_DEF.copy()


def get_word(list, number, delete=True):
    try:
        print(list[number])
        return list[number]
    except:
        print('Algo deu errado. Tente novamente')
        return 0

#print(len(PRESENTE_DEF))
print('\nPS: Se sua resposta for "leave" ou "sair" você volta para o menu de opções\n')

while True:
    try:
        choice = int(input('1 - Inglês para Português\n2 - Português para Inglês\n3 - Inglês para Português (clássico)\n4 - Reiniciar\n0 - Sair\n: '))
    except:
        print('ERRO: Tente novamente')
    
    # Sair
    if choice == 0:
        print('\n\033[34mSo long!\033[m')
        break
    #

    # Reiniciar
    if choice == 4:
        presente = PRESENTE_DEF
        print('\n\033[32mReiniciado com sucesso!\033[m\n')
        continue
    #

    while True:
        # Verificar se o programa foi finalizado
        if len(presente) == 0:
            print('\033[32mParabéns! Você finalizou o programa.\033[m')
            break
        #
        
        # Inglês para Português
        if choice == 1: 
            num = randint(0, len(presente) - 1)
            atual_list = presente[num]

            resp = str(input(f'O que significa {atual_list[0]}? ')).lower().strip(' ')

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
                if c == atual_list[1][-1]: # Se for o último
                    trad += f'{c}'
                else:
                    trad += f'{c}, '
            #
            
            # Mostrando dados
            print(f'Presente:\033[34m{atual_list[0] :>20}\033[m')
            print(f'Passado:\033[34m{atual_list[2] :>20}\033[m')
            print(f'Participio:\033[34m{atual_list[3] :>20}\033[m')
            print(f'\nPossíveis traduções: \033[33m{trad}\033[m\n')
            #

            print('\n' * 10)
        #

        # Português para Inglês
        elif choice == 2: 
            num = randint(0, len(presente) - 1)
            atual_list = presente[num]

            resp = str(input(f'O que significa {atual_list[1][0]}? ')).lower().strip(' ')

            # Sair
            if resp == 'leave' or resp == 'sair':
                break
            #
            
            # Acertou?
            if resp in atual_list[0]:
                print('\033[32mCorreto ✅\033[m')
                del(presente[num])
            else:
                print('\033[31mErrado ❌\033[m')
            #

            print()

            # Coletando traduções
            trad = ''
            for c in  atual_list[1]:
                if c == atual_list[1][-1]: # Se for o último
                    trad += f'{c}'
                else:
                    trad += f'{c}, '
            #
            
            # Mostrando dados
            print(f'Presente:\033[34m{atual_list[0] :>20}\033[m')
            print(f'Passado:\033[34m{atual_list[2] :>20}\033[m')
            print(f'Participio:\033[34m{atual_list[3] :>20}\033[m')
            print(f'\nPossíveis traduções: \033[33m{trad}\033[m\n')
            #

            print('\n' * 10)
        #

        #
        elif choice == 3: 
            num = randint(0, len(presente) - 1)
            atual_list = presente[num]

            print(f'Presente: \033[34m{atual_list[0]}\033[m')
            passsado = str(input(f'\033[mPassado: \033[34m')).lower().strip(' ')
            # Sair
            if passsado == 'leave' or passsado == 'sair':
                break
            #

            participio = str(input(f'\033[mParticipio: \033[34m')).lower().strip(' ')
            # Sair
            if participio == 'leave' or participio == 'sair':
                break
            #

            traducao = str(input(f'\033[mTraducao: \033[34m')).lower().strip(' ')
            # Sair
            if traducao == 'leave' or traducao == 'sair':
                break
            #

            print('\033[m')

            # Coletando traduções
            trad = ''
            for c in atual_list[1]:
                if c == atual_list[1][-1]: # Se for o último
                    trad += f'{c}'
                else:
                    trad += f'{c}, '
            #

            # Coletando variações
            passado_true = atual_list[2]
            participio_true = atual_list[3]
            #

            # Verifica os acertos
            if passado_true == passsado and participio_true == participio and traducao in trad: # Se o usuário acertar tudo
                del(presente[num]) # Deleto o verbo da lista
            #

            print(f'\t\t\033[1;34;40mRESPOSTAS\033[m')
            print('=' * 40)
            print()

            # Mostrando dados
            print(f'Presente:\033[34m{atual_list[0] :>20}\033[m') # Mostra o presente

            print(f'Passado:\033[34m{atual_list[2] :>20}\033[m', end=' ') # Mostra o passado
            if passado_true == passsado: # Verifica se o usuário acertou
                print('✅') # Informa se sim
            else: # Se errou
                print('❌') # Informa
            
            print(f'Participio:\033[34m{atual_list[3] :>20}\033[m', end=' ') # Mostra o particípio
            if participio_true == participio: # Verifica se o usuário acertou
                print('✅') # Informa que sim
            else: # Se não
                print('❌') # Informa que não
            
            print(f'\nPossíveis traduções: \033[33m{trad}\033[m', end=' ') # Mostra as possíveis traduções
            if traducao in trad: #Se tiver acertado
                print('✅') # Informa que sim
            else: # Se não
                print('❌') # Informa que não
            #

            print('\n' * 10) # Pula 10 linhas por organização
        #
            
        else:
            print()