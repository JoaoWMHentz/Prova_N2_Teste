import pytest
from stat_funcs import StatsN2
from conftest import fixture_numeros_amodal
stat = StatsN2()

def test_chamar_media():
    assert callable(stat.media)
    
@pytest.mark.parametrize("conjunto", [[1,45,4,4,34,6,67]])
@pytest.mark.parametrize("resultado", [23])
def test_media_parametrizado(conjunto, resultado):
    media = stat.media(conjunto)
    assert media == resultado
    
def test_media(fixture_numeros_amodal):
    media = stat.media(fixture_numeros_amodal)
    assert round(media,4) == 3.0000
    
def test_media_null():
    media = stat.media(None)
    assert media == 0