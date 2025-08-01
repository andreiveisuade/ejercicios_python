import pytest
from main import numerosPares

def test_numeros_pares_hasta_10():
    assert numerosPares(10) == [0, 2, 4, 6, 8, 10]

def test_numeros_pares_hasta_0():
    assert numerosPares(0) == [0]
