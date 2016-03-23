
import unittest


def bubble_sort(seq):

    '''
    :param seq:
    :return: seq ordenada

    Complexidade (Pior Caso)

    Tempo: O(n^2)
    Memória: O(1)

    Complexidade (Melhor Caso - Lista de entrada já está ordenada)

    Tempo: O(n)
    Memória: O(1)

    '''

    for i in range(len(seq)-1):

        for x in range(len(seq)-1):
            if seq[x] > seq[x+1]:
               seq[x], seq[x+1] = seq[x+1], seq[x]
               if i == 0: cont = 1
        if cont and cont != 1: break

    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
