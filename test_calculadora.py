import pytest
from calculadora import Calculadora

def test_soma_de_dois_numeros():
    calculadora = Calculadora()
    resultado = calculadora.somar(5,3)
    assert resultado == 8

def test_subtracao_de_dois_numeros_resultado_positivo():
    calculadora = Calculadora()
    resultado = calculadora.subtrair(8,6)
    assert resultado == 2

def test_subtracao_de_dois_numeros_resultado_negativo():
    calculadora = Calculadora()
    resultado = calculadora.subtrair(5,9)
    assert resultado == -4