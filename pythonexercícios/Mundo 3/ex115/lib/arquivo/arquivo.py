from ..interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # Abertura de arquivo para leitura no modo txt
        a.close() # Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # Cria e escreve um arquivo txt
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
