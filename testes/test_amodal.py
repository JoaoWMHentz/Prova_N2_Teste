import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_numeros_unimodal, fixture_numeros_multimodal, fixture_pesos
stat = StatsN2()

def test_chamar_multimodal():
    assert callable(stat.multimodal)
    
@pytest.mark.parametrize("conjunto", [[1,4,34,6,67]])
@pytest.mark.parametrize("resultado", ["Não existe moda"])
def test_amodal_parametrizado(conjunto, resultado):
    moda = stat.amodal(conjunto)
    assert moda == resultado
    
def test_amodal_multimodal(fixture_numeros_amodal):
    moda = stat.amodal(fixture_numeros_amodal)
    assert moda == "Não existe moda"
    
def test_amodal_nao_multimodal(fixture_numeros_unimodal):
    moda = stat.amodal(fixture_numeros_unimodal)
    assert moda == "Existe moda"
    
@pytest.mark.xfail(reason="Entra com uma multimodal")
def test_amodal_fail(fixture_numeros_multimodal):
    moda = stat.amodal(fixture_numeros_multimodal)
    assert moda == "Não existe moda"