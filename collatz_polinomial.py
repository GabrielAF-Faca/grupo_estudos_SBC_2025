

def multiplica_polinomio(p:list):
    p2 = [1, 1]
    res = [0] * (len(p) + len(p2) - 1)
    for o1, i1 in enumerate(p):
        for o2, i2 in enumerate(p2):
            res[o1 + o2] += i1 * i2
    res[0] += 1

    return res


def divide_polinomio(p:list):

    for i in range(1, len(p)):
        if p[i] == 1:
            p[i] = 0
            p[i-1] += 1


    if p[-1] == 0:
        p.pop(-1)


def zera_dois(p:list):
    for i in range(len(p)):
        if p[i] > 1:
            p[i] = 0


n = int(input())
a = list(map(int, input().split()))

a.reverse()

'''
3
1 0 0 1
'''
count = 0

while len(a) > 1:

    if a[0] == 1:
        a = multiplica_polinomio(a)
    else:
        divide_polinomio(a)

    zera_dois(a)

    count += 1

print(count)



