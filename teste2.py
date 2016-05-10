from collections import Counter


def quadrados_menores(n):
    quadrados = []
    for q in range(1, n + 1):
        if q ** 2 <= n and q ** 2 not in quadrados:
            quadrados.append(q ** 2)
        else:
            return quadrados
    return quadrados

def soma_quadrados(n):

    if n == 0:
        return [0]

    menores = quadrados_menores(n)
    if menores[-1] == n:
        return [n]
    else:
        lista_final = []
        lista_final.extend(gerar_solucao(menores, n))
        while menores:
            lista_transitoria = gerar_solucao(menores, n)
            if len(lista_transitoria) < len(lista_final):
                lista_final = lista_transitoria
    return lista_final

def gerar_solucao(menores, n):
    ultimo = menores.pop()
    lista_gerada = [ultimo]
    lista_gerada.extend(soma_quadrados(n - ultimo))
    return lista_gerada


import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))