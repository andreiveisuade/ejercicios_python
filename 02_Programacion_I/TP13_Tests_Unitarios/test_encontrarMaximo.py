import pytest
from main import encontrarMaximo

def test_encontrar_maximo_normal():
    assert encontrarMaximo([1, 5, 2, 8, 3]) == 8

def test_encontrar_maximo_lista_vacia():
    assert encontrarMaximo([]) is None
