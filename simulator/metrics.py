import numpy as np
from .config import FACTOR_LUMEN

def calcular_costo(
    tokens_entrada: np.ndarray,
    tokens_salida: np.ndarray,
    asignacion: np.ndarray,
    precios: np.ndarray
) -> np.ndarray:
    """
    Calcula el costo en USD de cada consulta utilizando Fancy Indexing sobre la matriz de precios.
    Incorpora el factor de calibración FACTOR_LUMEN.
    
    Retorna un arreglo con el costo en USD de cada consulta.
    """
    precio_entrada = precios[asignacion, 0]
    precio_salida  = precios[asignacion, 1]
    
    costo_base = (tokens_entrada * precio_entrada + tokens_salida * precio_salida) / 1_000_000.0
    costo_calibrado = costo_base * FACTOR_LUMEN
    
    return costo_calibrado


def evaluar_atencion(
    tokens_entrada: np.ndarray,
    asignacion: np.ndarray,
    capacidad: np.ndarray
) -> np.ndarray:
    """
    Evalúa si cada consulta fue bien atendida (True) o superó la capacidad del modelo asignado (False).
    
    Retorna un arreglo booleano del mismo tamaño que la entrada.
    """
    capacidad_asignada = capacidad[asignacion]
    return tokens_entrada <= capacidad_asignada
