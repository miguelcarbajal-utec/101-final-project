import numpy as np
import pytest
from simulator.config import PRECIOS, CAPACIDAD, UMBRALES
from simulator.policies import asignar_modelo, politica_todo_grande, politica_todo_pequeno
from simulator.metrics import calcular_costo, evaluar_atencion

def test_asignar_modelo_umbrales():
    tokens = np.array([50, 199, 200, 500, 999, 1000, 5000])
    asig = asignar_modelo(tokens, UMBRALES)
    esperado = np.array([0, 0, 1, 1, 1, 2, 2])
    assert np.array_equal(asig, esperado)

def test_calcular_costo_ejemplo_pdf():
    # Consulta de 1000 tokens entrada, 500 salida, modelo mediano (precios 3.00 y 15.00)
    # Costo esperado: (1000*3 + 500*15) / 1,000,000 = 0.0105
    t_in = np.array([1000])
    t_out = np.array([500])
    asig = np.array([1])
    costo = calcular_costo(t_in, t_out, asig, PRECIOS)
    assert np.isclose(costo[0], 0.0105)

def test_evaluar_atencion():
    tokens = np.array([150, 250, 900, 1200, 50000])
    asig = np.array([0, 0, 1, 1, 2])
    # Capacidad: [200, 1000, 1000000]
    # Esperado: [True, False, True, False, True]
    atencion = evaluar_atencion(tokens, asig, CAPACIDAD)
    assert np.array_equal(atencion, [True, False, True, False, True])
