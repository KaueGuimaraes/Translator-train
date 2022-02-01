def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()

def write(arquivo, content):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mOcorreu um ao o tentar cadastrar o usuário!\033[m')
    else:
        try:
            a.write(f'{content}\n')
        except:
            print('\033[31mOcorreu um erro ao tentar cadastrar o usuário!\033[m')
    finally:
        a.close()