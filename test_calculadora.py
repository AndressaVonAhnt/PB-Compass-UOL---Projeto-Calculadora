import pytest
from calculadora import Calculadora

def test_soma_de_dois_numeros():
    calculadora = Calculadora()
    resultado = calculadora.somar(5,3)
    assert resultado == 8