from math import ceil

linha = list(input())

sequence = []
current_best = []

for i in range(ceil(len(linha)/2)):

    popped = linha[i]
    sequence.append(popped)

    scale = len(linha)/len(sequence)
    if scale.is_integer():

        if sequence*int(scale) == linha:
            current_best = "".join(sequence)


print(current_best if current_best else -1)
