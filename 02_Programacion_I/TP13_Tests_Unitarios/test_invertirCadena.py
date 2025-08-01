import pytest
from main import invertirCadena

def test_invertir_cadena_normal():
    assert invertirCadena("hola") == "aloh"

def test_invertir_cadena_vacia():
    assert invertirCadena("") == ""
