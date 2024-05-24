import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal, fixture_pesos
stat = StatsN2()

def test_chamar_media():
    assert callable(stat.mediana)
    
@pytest.mark.parametrize("conjunto", [[1,4,5,1,4,6]])
@pytest.mark.parametrize("resultado", [4])
def test_mediana_parametrizado(conjunto, resultado):
    mediana = stat.mediana(conjunto)
    assert mediana == resultado
    
def test_mediana(fixture_numeros_amodal):
    media = stat.mediana(fixture_numeros_amodal)
    assert media == 3
    
def test_mediana_null():
    media = stat.mediana([])
    assert media == 0