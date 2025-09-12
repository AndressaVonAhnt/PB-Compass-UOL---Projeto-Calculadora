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

def test_multiplicacao_de_dois_numeros_positivos():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(2,9)
    assert resultado == 18

def test_multiplicacao_de_dois_numeros_negativos():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(-3,-2)
    assert resultado == 6

def test_multiplicacao_de_um_positivo_um_negativo():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(4,-2)
    assert resultado == -8

def test_multiplicacao_por_zero():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(6,0)
    assert resultado == 0

def test_multiplicacao_por_1():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(7,1)
    assert resultado == 7