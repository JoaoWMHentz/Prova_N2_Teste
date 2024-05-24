import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_numeros_unimodal, fixture_numeros_multimodal, fixture_pesos
stat = StatsN2()

def test_chamar_multimodal():
    assert callable(stat.variancia)
    
@pytest.mark.parametrize("conjunto", [[1,4,4,4,34,6,67]])
@pytest.mark.parametrize("resultado", [612.1429])
def test_variancia_parametrizado(conjunto, resultado):
    vari = stat.variancia(conjunto)
    assert round(vari, 4) == resultado
    
def test_variancia_unimodal(fixture_numeros_unimodal):
    vari = stat.variancia(fixture_numeros_unimodal)
    assert round(vari, 4) == 4.4762

    
@pytest.mark.xfail(reason="Entra com uma string")
def test_variancia_fail():
    moda = stat.variancia("String")
    assert True