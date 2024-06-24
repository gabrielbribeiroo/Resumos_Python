def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: o preço que quer se reajustar.
    :param taxa: qual é a porcentagem de aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Calcula a diminuição de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: o preço que quer se reajustar.
    :param taxa: qual é a porcentagem de redução.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    """
    -> Calcula o dobro de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: o preço que quer se reajustar.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    """
    -> Calcula a metade de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: o preço que quer se reajustar.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    """
    -> Formata o preço, a depender da moeda escolhida.
    :param preco: o preço informado.
    :param moeda: tipo de moeda escolhida (padrão: R$).
    :return: o valor formatado.
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxa=0, resp='A', formato=False):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    if resp == 'A':
        print(f'Com {taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    elif resp == 'D':
        print(f'Com {taxa}% de redução: \t{diminuir(preco, taxa, True)}')
    print('-'*30)