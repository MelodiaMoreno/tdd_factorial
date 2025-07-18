import pytest
from src.factorial import factorial

# def test_factorial_1_falla():
    # assert factorial(1) == 2  

def test_factorial_1_pasa():
    assert factorial(1) == 1

def test_tipo_falla():
    with pytest.raises(TypeError):
        factorial("texto")  

def test_tipo_pasa():
    assert factorial(3) == 6  

def test_negativo_falla():
    with pytest.raises(ValueError):
        factorial(-1)  

def test_negativo_pasa():
    assert factorial(0) == 1  

# def test_positivo_falla():
   # assert factorial(3) == 5  

def test_positivo_pasa():
    assert factorial(4) == 24