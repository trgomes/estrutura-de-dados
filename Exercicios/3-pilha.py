# -*- coding: utf-8 -*-

class PilhaVaziaErro(Exception):
    pass


class Pilha():
    def __init__(self):
        self.lista = []

    def topo(self):
        if self.lista:
            return self.lista[-1]
        raise PilhaVaziaErro()

    def vazia(self):
        return not bool(self.lista)

    def empilhar(self, valor):
        self.lista.append(valor)


    def desempilhar(self):
        try:
            return self.lista.pop()
        except IndexError:
            raise PilhaVaziaErro


import unittest


class PilhaTestes(unittest.TestCase):
    def test_topo_lista_vazia(self):
        pilha = Pilha()
        self.assertTrue(pilha.vazia())
        self.assertRaises(PilhaVaziaErro, pilha.topo)

    def test_empilhar_um_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.vazia())
        self.assertEqual('A', pilha.topo())

    def test_empilhar_dois_elementos(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        self.assertFalse(pilha.vazia())
        self.assertEqual('B', pilha.topo())

    def test_desempilhar_pilha_vazia(self):
        pilha = Pilha()
        self.assertRaises(PilhaVaziaErro, pilha.desempilhar)

    def test_desempilhar(self):
        pilha = Pilha()
        letras = 'ABCDE'
        for letra in letras:
            pilha.empilhar(letra)

        for letra_em_ordem_reversa in reversed(letras):
            letra_desempilhada = pilha.desempilhar()
            self.assertEqual(letra_em_ordem_reversa, letra_desempilhada)