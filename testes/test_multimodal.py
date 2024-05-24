import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_numeros_unimodal, fixture_numeros_multimodal, fixture_pesos
stat = StatsN2()

def test_chamar_multimodal():
    assert callable(stat.multimodal)
    
@pytest.mark.parametrize("conjunto", [[1,4,4,4,34,6,67]])
@pytest.mark.parametrize("resultado", ["Não é multimodal"])
def test_mulmodal_parametrizado(conjunto, resultado):
    moda = stat.multimodal(conjunto)
    assert moda == resultado
    
def test_multimodal_multimodal(fixture_numeros_multimodal):
    moda = stat.multimodal(fixture_numeros_multimodal)
    assert moda == [3,7]
    
def test_multimodal_nao_multimodal(fixture_numeros_unimodal):
    moda = stat.multimodal(fixture_numeros_unimodal)
    assert moda == "Não é multimodal"
    
@pytest.mark.xfail(reason="Entra com uma amodal")
def test_multimodal_fail(fixture_numeros_amodal):
    moda = stat.multimodal(fixture_numeros_amodal)
    assert moda == [3,7]