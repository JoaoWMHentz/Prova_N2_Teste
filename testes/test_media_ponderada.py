import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_pesos
stat = StatsN2()

def test_chamar_media():
    assert callable(stat.media_ponderada)
    
@pytest.mark.parametrize("conjunto", [[13,27,23,12,15]])
@pytest.mark.parametrize("resultado", [[19.5]])
@pytest.mark.parametrize("pesos", [[2,8,5,8,1]])
def test_media_ponderada_parametrizado(conjunto, resultado,pesos):
    media = stat.media_ponderada(conjunto,pesos)
    assert media == resultado
    
def test_media_ponderada(fixture_numeros_amodal, fixture_pesos):
    media = stat.media_ponderada(fixture_numeros_amodal, fixture_pesos)
    assert round(media, 4) == 2.3333
    
@pytest.mark.xfail(reason="Numero de conjunto e pesos em quantidades diferentes")
def test_media_ponderada_fail():
    media = stat.media_ponderada([4,3,5,5], [4,2,6])
    assert True