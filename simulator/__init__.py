"""
Simulador de Costos de un Asistente de IA Generativa
Materia: Programación 101 - Computación Científica en Python
"""

from .config import (
    MODELOS,
    PRECIOS,
    CAPACIDAD,
    UMBRALES,
    NUM_DIAS,
    CONSULTAS_POR_DIA,
    TOKENS_TIPICOS_ENTRADA,
    TOKENS_TIPICOS_SALIDA,
    DISPERSION,
    SEMILLA,
    FACTOR_LUMEN
)
from .generator import generar_consultas, descargar_y_procesar_dolly
from .policies import asignar_modelo, politica_todo_grande, politica_todo_pequeno
from .metrics import calcular_costo, evaluar_atencion
from .engine import ejecutar_simulacion, simular_con_presupuesto
from .visualizer import plot_dashboard, plot_comparativa_politicas

__all__ = [
    "MODELOS",
    "PRECIOS",
    "CAPACIDAD",
    "UMBRALES",
    "NUM_DIAS",
    "CONSULTAS_POR_DIA",
    "TOKENS_TIPICOS_ENTRADA",
    "TOKENS_TIPICOS_SALIDA",
    "DISPERSION",
    "SEMILLA",
    "FACTOR_LUMEN",
    "generar_consultas",
    "descargar_y_procesar_dolly",
    "asignar_modelo",
    "politica_todo_grande",
    "politica_todo_pequeno",
    "calcular_costo",
    "evaluar_atencion",
    "ejecutar_simulacion",
    "simular_con_presupuesto",
    "plot_dashboard",
    "plot_comparativa_politicas"
]
