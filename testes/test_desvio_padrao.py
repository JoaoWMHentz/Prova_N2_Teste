import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_numeros_unimodal, fixture_numeros_multimodal, fixture_pesos
stat = StatsN2()

def test_chamar_multimodal():
    assert callable(stat.dpadrao)
    
@pytest.mark.parametrize("conjunto", [612.1429])
@pytest.mark.parametrize("resultado", [24.7415])
def test_padrao_parametrizado(conjunto, resultado):
    depadrao = stat.dpadrao(conjunto)
    assert round(depadrao, 4) == resultado
    
def test_padrao():
    depadrao = stat.dpadrao(4.4762)
    assert round(depadrao, 4) == 2.1157

    
@pytest.mark.xfail(reason="Entra com uma string")
def test_padrao_fail():
    moda = stat.dpadrao("String")
    assert True