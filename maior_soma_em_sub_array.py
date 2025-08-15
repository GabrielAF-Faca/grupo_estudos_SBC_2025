
tamanho = int(input())

elementos = [int(i) for i in input().split(" ")]

sub_len = int(tamanho * (tamanho + 1) / 2)
index = 2
p = 1
corte = tamanho

best_sum = min(elementos)

for i in range(tamanho, sub_len):
    #print(i-corte, index)

    s = sum(elementos[i-corte: index])

    if s > best_sum:
        best_sum = s

    if index == tamanho:
        p += 1
        index = p
        corte = i + 1
    index += 1

print(best_sum)