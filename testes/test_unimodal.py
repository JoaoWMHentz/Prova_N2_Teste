import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_numeros_unimodal, fixture_numeros_multimodal, fixture_pesos
stat = StatsN2()

def test_chamar_multimodal():
    assert callable(stat.unimodal)
    
@pytest.mark.parametrize("conjunto", [[1,4,4,4,34,6,67]])
@pytest.mark.parametrize("resultado", [4])
def test_unimodal_parametrizado(conjunto, resultado):
    moda = stat.unimodal(conjunto)
    assert moda == resultado
    
def test_unimodal_unimodal(fixture_numeros_unimodal):
    moda = stat.unimodal(fixture_numeros_unimodal)
    assert moda == 4
    
def test_unimidal_nao_unimodal(fixture_numeros_multimodal):
    moda = stat.unimodal(fixture_numeros_multimodal)
    assert moda == "Não é unimodal"
    
@pytest.mark.xfail(reason="Entra com uma amodal")
def test_unimodal_fail(fixture_numeros_amodal):
    moda = stat.unimodal(fixture_numeros_amodal)
    assert moda == 4