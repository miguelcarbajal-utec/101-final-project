import numpy as np
import pytest
from simulator.config import (
    NUM_DIAS,
    CONSULTAS_POR_DIA,
    TOKENS_TIPICOS_ENTRADA,
    TOKENS_TIPICOS_SALIDA,
    DISPERSION,
    SEMILLA
)
from simulator.generator import generar_consultas

def test_generar_consultas_dimensiones():
    ent, sal = generar_consultas(
        NUM_DIAS, CONSULTAS_POR_DIA,
        TOKENS_TIPICOS_ENTRADA, TOKENS_TIPICOS_SALIDA,
        DISPERSION, SEMILLA
    )
    assert ent.shape == (30, 500)
    assert sal.shape == (30, 500)
    assert issubclass(ent.dtype.type, np.integer)
    assert issubclass(sal.dtype.type, np.integer)

def test_generar_consultas_minimo_un_token():
    ent, sal = generar_consultas(5, 100, 10, 10, 1.5, 99)
    assert (ent >= 1).all()
    assert (sal >= 1).all()

def test_reproducibilidad_semilla():
    ent1, sal1 = generar_consultas(5, 50, 300, 400, 0.8, 42)
    ent2, sal2 = generar_consultas(5, 50, 300, 400, 0.8, 42)
    assert np.array_equal(ent1, ent2)
    assert np.array_equal(sal1, sal2)
