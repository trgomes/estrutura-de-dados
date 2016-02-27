# -*- coding: utf-8 -*-

import unittest


def minimo(seq):
    if(seq == []):
        return None
    elif (len(seq) == 1):
        menor = seq[0]
    else:
        menor = minimo(seq[0:len(seq) - 1])

        if menor < seq[len(seq) - 1]:
            menor = menor
        else:
            menor = seq[len(seq) - 1]

    return menor;


def maximo(seq):
    if(seq == []):
        return None
    elif (len(seq) == 1):
        maior = seq[0]
    else:
        maior = maximo(seq[0:len(seq) - 1])

        if maior > seq[len(seq) - 1]:
            maior = maior
        else:
            maior = seq[len(seq) - 1]
    return maior


def min_max(seq):
    '''
    :param seq: uma sequencia
    :return: (min, max)
    Retorna tupla cujo primeiro valor mínimo (min) é o valor
    mínimo da sequencia seq.
    O segundo é o valor máximo (max) da sequencia

    Complexidade

    Tempo: O(n)
    Espaço: O(n)

    '''
    return minimo(seq), maximo(seq)

# seq = [1,3,5,8,45,6,9,0]
#
# menor, maior = min_max(seq)
#
# print(menor, maior)


# Testes ################################################
class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))


    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()