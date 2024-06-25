# Exceções e erros do python
'''
NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
EOFError
KeyboardInterrupt
OSError
MemoryError
ConnectionError
RuntimeError
'''

try: # Tente realizar a operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): # Erro de valor ou tipo
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError: # Erro de divisão por zero
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro: # Procura o erro encontrado
    print(f'O erro encontrado foi {erro.__cause__}')
else: # Deu certo
    print(f'O resultado é {r:.1f}')
finally: # Certo/falha
    print('Volte sempre! Muito obrigado!')