import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_numeros_unimodal, fixture_numeros_multimodal, fixture_pesos
stat = StatsN2()

def test_chamar_deitrib():
    assert callable(stat.skew)
    
@pytest.mark.parametrize("conjunto", [[1,4,4,4,34,6,67]])
@pytest.mark.parametrize("resultado", ["Distribuição positiva"])
def test_distrib_parametrizado(conjunto, resultado):
    sket = stat.skew(conjunto)
    assert sket == resultado
    
def test_skew_unimodal(fixture_numeros_unimodal):
    sket = stat.skew(fixture_numeros_unimodal)
    assert sket == "Distribuição negativa"

    
@pytest.mark.xfail(reason="Entra com uma string")
def test_skew_fail():
    moda = stat.skew("String")
    assert True