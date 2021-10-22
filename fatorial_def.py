# crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro indique o numero a calcular
# e o outro chamado show, que será o valor lógico (opcional) indicando se será mostrado na tela o processo do calculo
# ou não


def fatorial(a, b=1):
    """
    a indica o numero a ser executado o fatorial
    b pode ser definido como 0 para não mostrar o processo do calculo fatorial
    """
    f = 1
    if b == 1:
        for c in range(1, a+1):
            f *= c
            if c == a:
                print(f'{a} = {f}')
            else:
                print(c, 'x', end=' ')
    else:
        for c in range(1, a+1):
            f *= c
    return f


d = fatorial(5, 1)
print(d)
