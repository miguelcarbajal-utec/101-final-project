import numpy as np
import pandas as pd

def generar_consultas(
    num_dias: int,
    consultas_por_dia: int,
    tokens_tipicos_entrada: int,
    tokens_tipicos_salida: int,
    dispersion: float,
    semilla: int
) -> tuple[np.ndarray, np.ndarray]:
    """
    Genera matrices de tokens de entrada y salida para toda la simulación.
    Aplica una distribución de colas pesadas según el criterio de Huanchaco.
    
    Parámetros:
        num_dias: Número de días a simular.
        consultas_por_dia: Cantidad de consultas diarias.
        tokens_tipicos_entrada: Mediana de tokens de entrada (prompt).
        tokens_tipicos_salida: Mediana de tokens de salida (respuesta).
        dispersion: Dispersión sigma de la distribución lognormal.
        semilla: Semilla aleatoria para reproducibilidad.
        
    Retorna:
        tokens_entrada: np.ndarray de enteros con forma (num_dias, consultas_por_dia).
        tokens_salida:  np.ndarray de enteros con forma (num_dias, consultas_por_dia).
    """
    # Fijar la semilla
    np.random.seed(semilla)
    tamano = (num_dias, consultas_por_dia)
    
    # Generación con distribución lognormal
    raw_entrada = np.random.lognormal(
        mean=np.log(tokens_tipicos_entrada),
        sigma=dispersion,
        size=tamano
    )
    raw_salida = np.random.lognormal(
        mean=np.log(tokens_tipicos_salida),
        sigma=dispersion,
        size=tamano
    )
    
    # Garantizar mínimo 1 token y convertir a enteros
    tokens_entrada = np.clip(raw_entrada, a_min=1, a_max=None).astype(int)
    tokens_salida = np.clip(raw_salida, a_min=1, a_max=None).astype(int)
    
    return tokens_entrada, tokens_salida


def descargar_y_procesar_dolly(
    url: str = "https://huggingface.co/datasets/databricks/databricks-dolly-15k/resolve/main/databricks-dolly-15k.jsonl",
    ruta_csv_salida: str = "consultas_reales.csv"
) -> pd.DataFrame:
    """
    Descarga el dataset Dolly-15k, calcula tokens aproximados y exporta consultas_reales.csv.
    """
    textos = pd.read_json(url, lines=True)
    textos["instruction"] = textos["instruction"].fillna("")
    textos["context"] = textos["context"].fillna("")
    textos["response"] = textos["response"].fillna("")
    
    caracteres_entrada = textos["instruction"].str.len() + textos["context"].str.len()
    caracteres_salida  = textos["response"].str.len()
    
    reales = pd.DataFrame({
        "categoria": textos["category"],
        "tokens_entrada": (caracteres_entrada / 4.0).round().clip(lower=1).astype(int),
        "tokens_salida":  (caracteres_salida  / 4.0).round().clip(lower=1).astype(int)
    })
    
    reales.to_csv(ruta_csv_salida, index=False)
    return reales
