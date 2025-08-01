import pytest
from main import factorial

def test_factorial_de_5():
    assert factorial(5) == 120

def test_factorial_de_0():
    assert factorial(0) == 1

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)
