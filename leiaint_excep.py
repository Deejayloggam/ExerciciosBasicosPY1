# reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de um numero de tipo invalido.
# aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaint():
    b = input('NUMERO INTEIRO: ').strip()
    try:
        int(b)
    except (ValueError, KeyboardInterrupt, TypeError):
        while not b.isnumeric():
            print('ERRO :( ')
            b = input('NUMERO INTEIRO: ')
    finally:
        return b


def leiafloat():
    b = input('NUMERO REAL: ').strip()
    while True:
        try:
            float(b)
        except (ValueError, TypeError):
            print(':( erro')
            b = input('NUMERO REAL: ').strip()
        else:
            break
    return b


z = leiaint()
y = leiafloat()
