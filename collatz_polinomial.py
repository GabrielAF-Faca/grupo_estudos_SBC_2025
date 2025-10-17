

def multiplica_polinomio(p:list):
    '''
    Função que multiplica uma lista de coeficientes de um polinomio pelo polinomio (x + 1) ([1, 1])
    :param p: Polinomio a ser multiplicado
    :return: Polinomio multiplicado
    '''

    p2 = [1, 1]
    res = [0] * (len(p) + len(p2) - 1)
    for o1, i1 in enumerate(p):
        for o2, i2 in enumerate(p2):
            res[o1 + o2] += i1 * i2
    res[0] += 1

    return res


def divide_polinomio(p:list):
    '''
    Função que divide todos os coeficientes com grau maior que 0 de um polinomio por x
    :param p: Polinomio a ser dividido
    '''

    for i in range(1, len(p)):
        if p[i] == 1:
            p[i] = 0
            p[i-1] += 1


    if p[-1] == 0:
        p.pop(-1)


def zera_dois(p:list):
    '''
    Zera todos os coeficientes com valor maior ou igual a 2
    :param p: Polinomio a ser percorrido
    '''
    for i in range(len(p)):
        if p[i] > 1:
            p[i] = 0


n = int(input())
a = list(map(int, input().split()))

a.reverse()

count = 0

while len(a) > 1:

    if a[0] == 1:
        a = multiplica_polinomio(a)
    else:
        divide_polinomio(a)

    zera_dois(a)

    count += 1

print(count)


'''
3
1 0 0 1

2
1 0 1

2
1 0 0

0
1
'''
