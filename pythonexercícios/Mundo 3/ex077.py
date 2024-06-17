# Contando Vogais
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for posicao in palavras:  # para cada palavra da tupla...
    print(f'\nNa palavra {posicao.upper()} temos ',
          end='')  # escreva, pulando uma linha, .... PALAVRA ..., não pule linha e não dê espaço
    for letra in posicao:  # para cada letra na palavra
        if letra.lower() in 'aeiou':  # se as letras minúsculas das palavras forem vogais
            print(letra, end=' ')  # escreva as vogais de cada palavra, separadas por espaço
