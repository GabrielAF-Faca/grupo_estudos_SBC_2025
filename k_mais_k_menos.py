
def binomial_coeff(n, k):
    if k > n:
        return 0

    if k == 0 or k == n:
        return 1

    return binomial_coeff(n - 1, k - 1) + binomial_coeff(n - 1, k)


linha = input().split(" ")

n = int(linha[0])
k = int(linha[1])

coefs_t = [int(i) for i in input().split(" ")]
coefs_p = [int(i) for i in input().split(" ")]

coefs_t.reverse()
coefs_p.reverse()

index = n
binomial_coefs = []
multiply_index = 0
x_indexes = {}

for i in range(n+1):
    x_indexes[i] = []

for i in range(n+1):
    for j in range(n+1):
        r = binomial_coeff(i, j)
        if r == 0:
            break
        binomial_coefs.append(r)

binomial_coefs.reverse()

for i in range(n):
    p = 1
    for j in range(index+1):

        multiplicadores = binomial_coefs[multiply_index] * (k ** j)

        x_indexes[index-j].append(coefs_t[n - index] * multiplicadores)
        x_indexes[index-j].append(coefs_p[n - index] * multiplicadores * p)

        multiply_index += 1
        p*=-1
    index -= 1

x_indexes[0].append(coefs_t[-1])
x_indexes[0].append(coefs_p[-1])


for i in range(n+1):
    print(sum(x_indexes[i])%998244353, end=" " if i < n else "")


