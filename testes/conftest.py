from stat_funcs import StatsN2
import pytest

@pytest.fixture
def fixture_numeros_unimodal():
    return [1,2,4,4,5,6,7]

@pytest.fixture
def fixture_numeros_multimodal():
    return [1,2,3,3,5,7,7,8]
    
@pytest.fixture
def fixture_numeros_amodal():
    return [1,2,3,4,5]
    
@pytest.fixture
def fixture_pesos():
    return [5,4,3,2,1]
