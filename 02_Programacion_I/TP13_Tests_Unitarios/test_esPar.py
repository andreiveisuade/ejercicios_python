import pytest
from main import esPar

def test_esPar_con_par():
    assert esPar(4) == True

def test_esPar_con_impar():
    assert esPar(7) == False

def test_esPar_con_cero():
    assert esPar(0) == True
