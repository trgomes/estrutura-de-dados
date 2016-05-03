class Arco():
    def __init__(self, origem, destino, valor):
        self.valor = valor
        self.vertices = (origem, destino)

    def __hash__(self):
        return hash(self.vertices + (self.valor,))

    def __eq__(self, arco):
        return (self.valor,) + self.vertices == (arco.valor,) + arco.vertices

    def __repr__(self):
        return 'Arco({!r}, {!r}, {!r})'.format(self.vertices[0], self.vertices[1], self.valor)

    def oposto(self, param):
        if param == self.vertices[0]:
            return self.vertices[-1]
        return self.vertices[0]

import unittest


class ArcoTestes(unittest.TestCase):
    def teste_init(self):
        arco = Arco('origem', 'destino', 1)
        self.assertTupleEqual(('origem', 'destino'), arco.vertices)
        self.assertEqual(1, arco.valor)

    def teste_oposto(self):
        arco = Arco('origem', 'destino', 1)
        self.assertEqual('origem', arco.oposto('destino'))
        self.assertEqual('destino', arco.oposto('origem'))


# Dados a serem usados nos testes

# Dados de vérticos
bertioga = 'Bertioga'
caragua = 'Caragua'
jacarei = 'Jacareí'
mogi = 'Mogi da Cruzes'
santos = 'Santos'
sjc = 'São José dos Campos'
sao_paulo = 'São Paulo'
taubate = 'Taubaté'

vertices_cidades = (bertioga,
                    caragua,
                    jacarei,
                    mogi,
                    santos,
                    sjc,
                    sao_paulo,
                    taubate)
# Dados de arcos
arco_tauba_sjc = Arco(taubate, sjc, 43900)
arco_scj_jaca = Arco(sjc, jacarei, 13200)
arco_scj_caragua = Arco(sjc, caragua, 86900)
arco_caragua_bertioga = Arco(caragua, bertioga, 114000)
arco_bertioga_mogi = Arco(bertioga, mogi, 48700)
arco_mogi_jaca = Arco(mogi, jacarei, 54300)
arco_mogi_sp = Arco(mogi, sao_paulo, 61900)
arco_jaca_sp = Arco(jacarei, sao_paulo, 81800)
arco_santos_sp = Arco(santos, sao_paulo, 72800)
arco_santos_bertioga = Arco(santos, bertioga, 74400)

arcos_distancias = (arco_tauba_sjc,
                    arco_scj_jaca,
                    arco_scj_caragua,
                    arco_caragua_bertioga,
                    arco_bertioga_mogi,
                    arco_mogi_jaca,
                    arco_mogi_sp,
                    arco_jaca_sp,
                    arco_santos_sp,
                    arco_santos_bertioga)


class Grafo():

    def __init__(self):
        self.vertice = ()
        self.arco = ()
        self.adjacencia = {}


    def vertices(self):
        return self.vertice

    def adicionar_vertice(self, nome_vertice):
        self.vertice += nome_vertice,


    def arcos(self, nome_arco):

        arco = ()
        for x in self.arco:
            if nome_arco in x.vertices:
                arco += x,
        return arco

    def adicionar_arco(self, arco):
        self.arco += arco,
        vertice_1 = arco.vertices[0]
        vertice_2 = arco.vertices[1]
        for cidade in self.vertice:
            if cidade in arco.vertices:
                if cidade not in self.adjacencia:
                    if cidade != vertice_1:
                        self.adjacencia[cidade] = (vertice_1, arco)
                    else:
                        self.adjacencia[cidade] = (vertice_2, arco)
                else:
                    if cidade != vertice_1:
                        self.adjacencia[cidade] += (vertice_1, arco)
                    else:
                        self.adjacencia[cidade] += (vertice_2, arco)

    def adjacencias(self, cidade):
        if self.adjacencia:
            adjacencias = ()
            for x in range(0, len(self.adjacencia[cidade]), 2):
                adjacencias += self.adjacencia[cidade][x],

            # print(adjacencias)
            return adjacencias
        return self.adjacencia




    def caminho(self, vertice1, vertice2):
        if vertice1 == vertice2:
            return [vertice1]
        elif self.arco == ():
            return []
        elif vertice2 in self.adjacencia[vertice1][0]:
            return [vertice1, vertice2]
        else:
            cidade_atual = vertice1
            lista = []
            lista.append(cidade_atual)
            while True:
                for cidade in self.adjacencia:
                    if cidade == cidade_atual:
                        for origem in self.adjacencia[cidade]:
                            if isinstance(origem, Arco) and (origem.vertices[0] not in lista or origem.vertices[1] not in lista):
                                if origem.vertices[0] != cidade:
                                    cidade_atual = origem.vertices[0]
                                    break
                                else:
                                    cidade_atual = origem.vertices[1]
                                    break
                        lista.append(cidade_atual)
                    if cidade_atual == vertice2:
                        return lista

    def calcular_melhores_caminhos_partindo_de(self, vertice):

        caminho = {vertice: [vertice]}
        visitados = [vertice]
        atual = {vertice: 0}


        while (len(visitados) < len(self.vertice)):
            for vert in self.arcos(vertice):
                if vert.oposto(vertice) not in visitados:
                    if vert.oposto(vertice) not in atual.keys():
                        atual[vert.oposto(vertice)] = atual[vertice] + vert.valor
                    else:
                        if atual[vert.oposto(vertice)] > atual[vertice] + vert.valor:
                            atual[vert.oposto(vertice)] = atual[vertice] + vert.valor

            for x, y in atual.items():
                if x not in visitados:
                    menor = y
                    ponto = x
                    break
            for x, y in atual.items():
                if x not in visitados:
                    if y < menor:
                        menor = y
                        ponto = x

            if ponto not in visitados:
                visitados.append(ponto)
            vertice = ponto
            for x in self.arcos(vertice):
                if x.oposto(ponto) in visitados:
                    menor = atual[x.oposto(vertice)] + x.valor
                    break

            for x in self.arcos(vertice):
                if x.oposto(vertice) in visitados:

                    if atual[x.oposto(vertice)] + x.valor <= menor:
                        menor = atual[x.oposto(vertice)] + x.valor
                        ponto = x.oposto(vertice)
                        val = x.valor

            caminho[vertice] = caminho[ponto] + [val, vertice]
        cam = {}
        for x, y in atual.items():
            cam[x] = tuple()
            cam[x] = cam[x] + (y, caminho[x])
        return cam





class GrafoTestes(unittest.TestCase):
    def teste_adicionar_vertice(self):
        grafo = Grafo()
        self.assert_mesmo_elementos(tuple(), grafo.vertices())
        grafo.adicionar_vertice(santos)
        self.assert_mesmo_elementos((santos,), grafo.vertices())
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos((santos, jacarei), grafo.vertices())
        grafo.adicionar_vertice(mogi)
        self.assert_mesmo_elementos((santos, jacarei, mogi), grafo.vertices())
        grafo.adicionar_vertice(caragua)
        self.assert_mesmo_elementos((santos, jacarei, mogi, caragua), grafo.vertices())

    def teste_adicionar_arco(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(sjc))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(sjc))
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(jacarei))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(sjc))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(jacarei))
        grafo.adicionar_arco(arco_scj_jaca)
        self.assert_mesmo_elementos((arco_scj_jaca,), grafo.arcos(jacarei))
        self.assert_mesmo_elementos((arco_scj_jaca,), grafo.arcos(sjc))
        self.assert_mesmo_elementos((jacarei,), grafo.adjacencias(sjc))
        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(jacarei))
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_tauba_sjc)
        self.assert_mesmo_elementos((arco_scj_jaca, arco_tauba_sjc), grafo.arcos(sjc))
        self.assert_mesmo_elementos((arco_tauba_sjc,), grafo.arcos(taubate))

        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(jacarei))
        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(taubate))
        self.assert_mesmo_elementos((taubate, jacarei), grafo.adjacencias(sjc))

    def teste_caminho_para_proprio_vertice(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assertListEqual([sjc], grafo.caminho(sjc, sjc))

    def teste_caminho_vertices_desconexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        self.assertListEqual([], grafo.caminho(sjc, jacarei))

    def teste_caminho_dois_vertices_conexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_arco(arco_scj_jaca)
        self.assertListEqual([sjc, jacarei], grafo.caminho(sjc, jacarei))

    def teste_caminho_tres_vertices_conexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_scj_jaca)
        grafo.adicionar_arco(arco_tauba_sjc)

        self.assertListEqual([taubate, sjc, jacarei], grafo.caminho(taubate, jacarei))
        self.assertListEqual([taubate, sjc], grafo.caminho(taubate, sjc))

    def teste_caminho_4_vertices_conexos_nao_lineares(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_vertice(mogi)
        grafo.adicionar_vertice(sao_paulo)
        grafo.adicionar_arco(arco_scj_jaca)
        grafo.adicionar_arco(arco_jaca_sp)
        grafo.adicionar_arco(arco_mogi_jaca)
        grafo.adicionar_arco(arco_mogi_sp)

        caminho = grafo.caminho(sjc, sao_paulo)
        self.assertTrue([sjc, jacarei, sao_paulo] == caminho or [sjc, jacarei, mogi, sao_paulo] == caminho)

    def teste_melhor_caminho_partindo_de_taubate_considerando_distancias(self):
        grafo = Grafo()
        for v in vertices_cidades:
            grafo.adicionar_vertice(v)

        for a in arcos_distancias:
            grafo.adicionar_arco(a)

        dct = grafo.calcular_melhores_caminhos_partindo_de(taubate)
        self.assert_mesmo_elementos(vertices_cidades, dct.keys())

        distancia, caminho = dct[taubate]
        self.assertEqual(0, distancia)
        self.assertListEqual([taubate], caminho)

        distancia, caminho = dct[sjc]
        self.assertEqual(43900, distancia)
        self.assertListEqual([taubate, 43900, sjc], caminho)

        distancia, caminho = dct[jacarei]
        self.assertEqual(57100, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei], caminho)

        distancia, caminho = dct[mogi]
        self.assertEqual(111400, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 54300, mogi], caminho)

        distancia, caminho = dct[caragua]
        self.assertEqual(130800, distancia)
        self.assertListEqual([taubate, 43900, sjc, 86900, caragua], caminho)

        distancia, caminho = dct[sao_paulo]
        self.assertEqual(138900, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 81800, sao_paulo], caminho)

        distancia, caminho = dct[bertioga]
        self.assertEqual(160100, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 54300, mogi, 48700, bertioga], caminho)

        distancia, caminho = dct[santos]
        self.assertEqual(211700, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 81800, sao_paulo, 72800, santos], caminho)

    def teste_melhor_caminho_partindo_de_taubate_considerando_custo(self):
        grafo = Grafo()
        for v in vertices_cidades:
            grafo.adicionar_vertice(v)

        preco_gasolina = 3.65  # R$/litro
        rendimento_carro_popular = 15000  # metros/litro
        preco_por_distancia = preco_gasolina / rendimento_carro_popular  # R$/metro
        arcos_custo = [Arco(a.vertices[0], a.vertices[1], a.valor * preco_por_distancia)
                       for a in arcos_distancias]

        pedagios = {(jacarei, sao_paulo): 11.8, (jacarei, mogi): 6.1, (sao_paulo, santos): 23, (sao_paulo, mogi): 3.2,
                    (bertioga, santos): 10.8}

        for a in arcos_custo:
            vertices_contrarios = (a.vertices[1], a.vertices[0])
            pedagio = pedagios.get(a.vertices, pedagios.get(vertices_contrarios, 0))
            a.valor = round(pedagio + a.valor)

            grafo.adicionar_arco(a)

        dct = grafo.calcular_melhores_caminhos_partindo_de(taubate)
        self.assert_mesmo_elementos(vertices_cidades, dct.keys())

        distancia, caminho = dct[taubate]
        self.assertEqual(0, distancia)
        self.assertListEqual([taubate], caminho)

        distancia, caminho = dct[sjc]
        self.assertEqual(11, distancia)
        self.assertListEqual([taubate, 11, sjc], caminho)

        distancia, caminho = dct[jacarei]
        self.assertEqual(14, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei], caminho)

        distancia, caminho = dct[mogi]
        self.assertEqual(33, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 19, mogi], caminho)

        distancia, caminho = dct[caragua]
        self.assertEqual(32, distancia)
        self.assertListEqual([taubate, 11, sjc, 21, caragua], caminho)

        distancia, caminho = dct[sao_paulo]
        self.assertEqual(46, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 32, sao_paulo], caminho)

        distancia, caminho = dct[bertioga]
        self.assertEqual(45, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 19, mogi, 12, bertioga], caminho)

        distancia, caminho = dct[santos]
        self.assertEqual(74, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 19, mogi, 12, bertioga, 29, santos], caminho)

    def assert_mesmo_elementos(self, iteravel, outro_iteravel):
        "Método auxiliar para asserção de elementos"
        self.assertSetEqual(set(iteravel), set(outro_iteravel))