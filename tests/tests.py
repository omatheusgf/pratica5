import pytest
from program import *

def test_horas_para_minutos():
    assert horas_para_minutos(2) == 120
    with pytest.raises(ValueError):
        horas_para_minutos(-1)

def test_minutos_para_segundos():
    assert minutos_para_segundos(3) == 180
    with pytest.raises(ValueError):
        minutos_para_segundos(-5)

def test_segundos_para_horas():
    assert segundos_para_horas(3600) == 1
    assert segundos_para_horas(1800) == 0.5

def test_dias_para_horas():
    assert dias_para_horas(2) == 48
    with pytest.raises(ValueError):
        dias_para_horas(-2)

def test_horas_para_dias():
    assert horas_para_dias(48) == 2
    with pytest.raises(ValueError):
        horas_para_dias(-8)
