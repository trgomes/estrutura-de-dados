import unittest
from collections import deque
from itertools import product

regra = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wzyz'}


def gerar_alfa(s):
    """
    Fazer análise de tempo e espaço

    Função recebe string com números de 2 a 9 e responde todas sequencias possíveis de letras
    Reg

    Complexidade:

    Tempo: O(n**2)

    Espaço: O(n)
    """
    reg = deque([()])

    for n in s:

        cont = len(reg)

        while(cont > 0):
            ultimo = reg.popleft()
            letras = regra[n]
            for l in letras:
                reg.append(ultimo+(l,))

            cont -= 1

            # anterior = reg.pop()

    # print(reg)
    return reg




class Testes(unittest.TestCase):
    def testes_string_vazia(self):
        self.assertListEqual([tuple()], list(gerar_alfa('')))

    def testes_string_2(self):
        self.assertListEqual([('a',), ('b',), ('c',)], list(gerar_alfa('2')))

    def testes_string_3(self):
        self.assertListEqual([('d',), ('e',), ('f',)], list(gerar_alfa('3')))

    def testes_string_com_2_numeros(self):
        self.assertSetEqual(set((('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
                                 ('c', 'e'), ('c', 'f'))), set(gerar_alfa('23')))

    def testes_com_5_numeros(self):
        resultado = set(gerar_alfa('73696'))
        self.assertIn(tuple('renzo'), resultado)
        self.assertSetEqual(set(product('pqrs', 'def', 'mno', 'wzyz', 'mno')), resultado)
