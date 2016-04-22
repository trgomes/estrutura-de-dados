from collections import deque


def calcular_frequencias(s):

    if len(s) == 0:
        return {}
    else:
        seq = {}
        for i in range(len(s)):
            if i != 0 and s[i] in s[0 : i]:
                continue
            else:
                seq[s[i]] = s.count(s[i])

    return seq


def gerar_arvore_de_huffman(s):
    seq = calcular_frequencias(s)

    lista_de_tuplas = ([(valor, chave) for chave, valor in seq.items()])

    lista_ordenada = deque(sorted(lista_de_tuplas))

    while len(lista_ordenada) != 0:

        if len(lista_ordenada) == 1:
            return lista_ordenada[0][-1]

        primeiro = lista_ordenada.popleft()
        segundo = lista_ordenada.popleft()

        if isinstance(primeiro[-1], Arvore) and isinstance(segundo[-1], Arvore):
            arvore_fundida = primeiro.fundir(segundo)
        elif isinstance(primeiro[-1], Arvore):
            arvore = Arvore(segundo[-1], segundo[0])
            arvore_fundida = primeiro[-1].fundir(arvore)
        elif isinstance(segundo[-1], Arvore):
            arvore = Arvore(primeiro[-1], primeiro[0])
            arvore_fundida = arvore.fundir(segundo[-1])
        else:
            arvore1 = Arvore(primeiro[-1], primeiro[0])
            arvore2 = Arvore(segundo[-1], segundo[0])
            arvore_fundida = arvore1.fundir(arvore2)

        lista_ordenada.append((arvore_fundida.peso, arvore_fundida))

        lista_ordenada = deque(sorted(lista_ordenada))

    return arvore_fundida


def codificar(cod_dict, s):
    dic = cod_dict

    cod = ""

    for i in s:
        if i in dic.keys():
            cod += dic[i]

    return cod


class Noh:

    def __init__(self, peso, esquerdo = None, direito = None):
        self.peso = peso
        self.esquerdo = esquerdo
        self.direito = direito

    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh):
            return False
        return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito


class Folha():
    def __init__(self, char, peso):
        self.char = char
        self.peso = peso

    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha):
            return False
        return self.__dict__ == other.__dict__


class Arvore(object):
    def __init__(self, char = None, peso = None):
        self.char = char
        self.peso = peso

        if self.char:
            self.raiz = Folha(self.char, self.peso)
        else:
            self.raiz = None


    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if other is None:
            return False
        return self.raiz == other.raiz

    # Implementar
    def fundir(self, arvore):

        if self.peso > arvore.peso:
            maior = self.raiz
            menor = arvore.raiz
        else:
            maior = arvore.raiz
            menor = self.raiz

        peso = self.peso + arvore.peso
        raiz = Noh(peso, maior, menor)

        novaArvore = Arvore(peso=peso)

        novaArvore.raiz = raiz

        return novaArvore


    # Codificar
    def cod_dict(self):
        dic = {}
        caminho = []
        visitar = []

        visitar.append(self.raiz)

        while len(visitar) != 0:
            atual = visitar.pop()
            # print(atual.direito.peso, atual.esquerdo.char)

            # if type(atual) is Folha:
            if isinstance(atual, Folha):
                letra = atual.char
                dic[letra] = ''.join(caminho)
                caminho.pop()
                caminho.append('1')
            else:
                visitar.append(atual.direito)
                visitar.append(atual.esquerdo)
                caminho.append('0')

        return dic


    # Decodificar
    def decodificar(self, caminho):
        # print(self.raiz.peso)

        letras = []
        atual = self.raiz

        if isinstance(atual, Folha):
            return atual.char
        else:
            for i in caminho:
                if i == '0':
                    atual = atual.esquerdo
                else:
                    atual = atual.direito

                if isinstance(atual, Folha):
                    letras.append(atual.char)
                    atual = self.raiz

        return ''.join(letras)



from unittest import TestCase


class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))


class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)


def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada


class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)

        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', codificar(arvore.cod_dict(), 'aaaabbc'))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))
