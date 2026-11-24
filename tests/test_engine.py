import numpy as np
import pandas as pd
import pytest
from simulator.config import PRECIOS, CAPACIDAD, UMBRALES, NUM_DIAS, CONSULTAS_POR_DIA
from simulator.generator import generar_consultas
from simulator.policies import asignar_modelo, politica_todo_grande, politica_todo_pequeno
from simulator.engine import ejecutar_simulacion

@pytest.fixture
def matrices_simulacion():
    # Generamos matrices pequeñas para prueba rápida (5 días x 100 consultas)
    return generar_consultas(5, 100, 300, 400, 0.8, 42)

def test_ejecutar_simulacion_estructura(matrices_simulacion):
    mat_in, mat_out = matrices_simulacion
    politica = lambda t: asignar_modelo(t, UMBRALES)
    
    df = ejecutar_simulacion(mat_in, mat_out, politica, PRECIOS, CAPACIDAD)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    
    columnas_esperadas = [
        "dia", "cantidad_consultas", "tokens_entrada_total", "tokens_salida_total",
        "costo_dia", "costo_acumulado", "consultas_bien_atendidas", "pct_bien_atendidas",
        "consultas_pequeno", "consultas_mediano", "consultas_grande",
        "costo_pequeno", "costo_mediano", "costo_grande"
    ]
    for col in columnas_esperadas:
        assert col in df.columns, f"Falta la columna obligatoria: {col}"

def test_ejecutar_simulacion_consistencia_financiera_y_operativa(matrices_simulacion):
    mat_in, mat_out = matrices_simulacion
    politica = lambda t: asignar_modelo(t, UMBRALES)
    
    df = ejecutar_simulacion(mat_in, mat_out, politica, PRECIOS, CAPACIDAD)
    
    # 1. Conteo de consultas desglosadas debe sumar el total diario
    suma_consultas = df["consultas_pequeno"] + df["consultas_mediano"] + df["consultas_grande"]
    assert (suma_consultas == df["cantidad_consultas"]).all()
    
    # 2. Suma de costos por modelo debe aproximarse al costo diario
    suma_costos = df["costo_pequeno"] + df["costo_mediano"] + df["costo_grande"]
    assert np.allclose(suma_costos, df["costo_dia"], atol=1e-3)
    
    # 3. Costo acumulado debe coincidir con la suma acumulada de costo_dia
    assert np.allclose(df["costo_acumulado"], df["costo_dia"].cumsum(), atol=1e-3)
    
    # 4. Consultas bien atendidas no pueden superar el total
    assert (df["consultas_bien_atendidas"] <= df["cantidad_consultas"]).all()
    assert (df["pct_bien_atendidas"] >= 0.0).all() and (df["pct_bien_atendidas"] <= 100.0).all()
