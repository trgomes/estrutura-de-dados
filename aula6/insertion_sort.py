import unittest


def insertion_sort(seq):
    '''
    :param seq:
    :return: seqência ordenada

    Complexidade:

    Tempo = O(n**2)
    Memória = O(1)
    '''

    # if seq == sorted(seq):
    #         return seq

    for i in range(1,len(seq)):
        x = i # x  =  atul
        y = x -1 # y = anterior

        while seq[x] < seq[y] and x > 0:
            seq[x], seq[y] = seq[y], seq[x]
            y -= 1
            x -= 1
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()

