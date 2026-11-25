import numpy as np

# 1. Catálogo de Modelos y Nivel de Servicio
MODELOS = ["pequeno", "mediano", "grande"]

# 2. Matriz de Precios (3 x 2): [Precio Entrada, Precio Salida] por millón de tokens (USD)
PRECIOS = np.array([
    [0.25,  1.25],   # 0: pequeno
    [3.00, 15.00],   # 1: mediano
    [15.00, 75.00]   # 2: grande
], dtype=np.float64)

# 3. Capacidad máxima de tokens de entrada atendidos con calidad aceptable
CAPACIDAD = np.array([200, 1000, 1_000_000], dtype=np.int64)

# 4. Umbrales de asignación para la regla por tamaño (Política 1)
UMBRALES = [200, 1000]

# 5. Parámetros temporales y de tráfico
NUM_DIAS = 30
CONSULTAS_POR_DIA = 500

# 6. Parámetros estadísticos de la distribución lognormal
TOKENS_TIPICOS_ENTRADA = 300
TOKENS_TIPICOS_SALIDA = 400
DISPERSION = 0.8

# 7. Semilla de reproducibilidad
SEMILLA = 42
