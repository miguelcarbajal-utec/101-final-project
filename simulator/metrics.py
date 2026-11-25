import numpy as np

def calcular_costo(
    tokens_entrada: np.ndarray,
    tokens_salida: np.ndarray,
    asignacion: np.ndarray,
    precios: np.ndarray
) -> np.ndarray:
    """
    Calcula el costo en USD de cada consulta utilizando Fancy Indexing sobre la matriz de precios.
    
    Retorna un arreglo con el costo en USD de cada consulta.
    """
    precio_entrada = precios[asignacion, 0]
    precio_salida  = precios[asignacion, 1]
    
    costo = (tokens_entrada * precio_entrada + tokens_salida * precio_salida) / 1_000_000.0
    
    return costo


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
