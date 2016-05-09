from collections import Counter
from collections import deque

def soma_quadrados(n):



    resultados = {0:[0], 1:[1]}

    cont = 2
    num = n

    if n == 0 or n==1:
        return resultados[n]
    else:

        while cont <= num:
            n = cont
            quadrados = []

            for q in range(1,n+1):
                if q**2 <= n:
                    quadrados.append(q**2)

            print(quadrados)

            entrada = n
            listaAux = []
            aux = n
            while n not in resultados.keys() and n != 0:
                if quadrados and n not in quadrados:
                    while aux >= n and quadrados and aux != n-aux:
                        aux = quadrados.pop()

                n = n - aux
                listaAux.append(aux)

            print("listaAux",listaAux)


            cont += 1

            if n == 0:
                resultados[entrada] = listaAux
            else:
                listaAtual = listaAux
                listaAnterior = resultados[n]
                resultados[entrada]= listaAtual.__add__(listaAnterior)


        # print(listaAtual, listaAnterior)

    # print("Aqui",quadrados)
    print(resultados)

    return resultados[entrada]


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