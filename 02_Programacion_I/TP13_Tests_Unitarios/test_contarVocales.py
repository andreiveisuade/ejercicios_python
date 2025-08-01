import pytest
from main import contarVocales

def test_contar_vocales_normal():
    assert contarVocales("murcielago") == 5

def test_contar_vocales_mayusculas():
    assert contarVocales("AEIOU") == 5

def test_contar_vocales_sin_vocales():
    assert contarVocales("rhythm") == 0
