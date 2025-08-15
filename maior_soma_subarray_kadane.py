def soma_maxima_subarray(elementos):

    if not elementos:
        return 0

    max_global = elementos[0]
    max_atual = elementos[0]

    for i in range(1, len(elementos)):
        numero_atual = elementos[i]

        # O sub-array máximo que termina aqui é ou o número atual sozinho,
        # ou o número atual adicionado ao sub-array máximo anterior.
        max_atual = max(numero_atual, max_atual + numero_atual)

        # Atualiza a soma máxima global se encontrarmos uma maior.
        if max_atual > max_global:
            max_global = max_atual

    return max_global


# --- Como usar com a sua entrada ---
tamanho = int(input())
elementos = [int(i) for i in input().split(" ")]

best_sum = soma_maxima_subarray(elementos)

print(best_sum)