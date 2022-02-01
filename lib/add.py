from arquivo import * # Importar cada função do arquivo


lista = list() # Crio uma lista
cont = 0 # Inicio o contador

color = '\033[32m' # Escolho a cor principal
color_final = '\033[m' # Seto a cor final

leave = False # Falo que o usuário não quer sair

while True: # Enquanto verdadeiro
    while True: # Enquanto verdadeiro
        presente = str(input(f'{color}Presente:{color_final} ')).lower() # Pergunta ao usuário o presente
        if presente == 'mostre-me' or presente == 'show-me': # Se o usuário pedir para mostras as informações
            cont = 0 # O contador será igual a 0
            for c in lista: # Para cada item na lista
                cont += 1 # o contador será += 1
                if cont == 1: # Se o contador for 1
                    print(f'\n{c},\t', end='') # Vai mostrar no início da linha
                elif cont == 2: # Se não caso ele seja igual a 2
                    print(f'{c},', end='') # Vai mostrar no final da linha
                    cont = 0 # E o contador será igual a 0
            cont = 0 # O contador será igual a 0
            print('\n\n') # Irei pular 2 linhas
        elif presente == 'saia': # Se não se o usuário quiser sair do programa
            leave = True # Sair será verdadeiro
            break # Saio do looping
        else: # Se não
            break # Saio do looping

    if leave: # Se ele quiser sair
        print('\nCaso queira a lista, lembre-se de consultar o save temporario!') # Aviso o usuário sobre o save
        print('\033[34mSo long!\033[m') # Digo adeus
        break # Fecho o programa

    passado = str(input(f'{color}Passado:{color_final} ')).lower() # Pergunta o passado
    participio = str(input(f'{color}Participio:{color_final} ')).lower() # Pergunta o participio

    portugues = str(input(f'\n{color}Traducoes:{color_final} ')).lower().replace(' ', '').split(',') # Pergunta as traduções em Inglês
    print() # Pulo uma linha

    lista.append([presente, portugues, passado, participio]) # Adiciona a lista
    save = '' # Cria a variavel do save
    
    cont = 0 # O contador será igual a 0
    for c in lista: # Para cada item na lista
        cont += 1 # Contador mais igual a 1
        if cont == 1: # Se o contador for igual a 1
            save += f'{c},\t' # Vou adicionar no começo da linha
        elif cont == 2:
            save += f'{c},\n' # Vou adicionar no final da linha
            cont = 0 # E o contador voltará a ser igual a 0
    cont = 0 # O contador será igual a 0

    criarArquivo('save.txt') # Resetarei o save
    write('save.txt', save) # Salvo