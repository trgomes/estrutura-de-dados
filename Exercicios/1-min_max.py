# -*- coding: utf-8 -*-

def maximo(seq):
    if (len(seq) == 1):
        maior = seq[0]
    else:

        maior = maximo(seq[0:len(seq) - 1])

        if maior > seq[len(seq) - 1]:
            maior = maior
        else:
            maior = seq[len(seq) - 1]
    return maior


def minimo(seq):
    if (len(seq) == 1):
        menor = seq[0]
    else:

        menor = minimo(seq[0:len(seq) - 1])

        if menor < seq[len(seq) - 1]:
            menor = menor
        else:
            menor = seq[len(seq) - 1]

    return menor;


seq = [2, 75, 8, 3, 1, 60, 15, 6, 0]


print(maximo(seq))
print('\n')
print(minimo(seq))