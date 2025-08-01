import pytest
from main import esPalindromo

def test_esPalindromo_verdadero():
    assert esPalindromo("neuquen") == True
    assert esPalindromo("Anita lava la tina") == True

def test_esPalindromo_falso():
    assert esPalindromo("hola") == False
