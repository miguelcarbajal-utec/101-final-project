import numpy as np
import pandas as pd
from typing import Callable
from .metrics import calcular_costo, evaluar_atencion
from .policies import asignar_modelo

def ejecutar_simulacion(
    matriz_entrada: np.ndarray,
    matriz_salida: np.ndarray,
    politica_asignacion: Callable[[np.ndarray], np.ndarray],
    precios: np.ndarray,
    capacidad: np.ndarray
) -> pd.DataFrame:
    """
    Ejecuta la simulación mensual recorriendo día a día (único bucle for permitido).
    
    Parámetros:
        matriz_entrada: np.ndarray de forma (num_dias, consultas_por_dia)
        matriz_salida:  np.ndarray de forma (num_dias, consultas_por_dia)
        politica_asignacion: Función que asigna modelos a un vector de tokens de entrada
        precios: Matriz de tarifas (3, 2)
        capacidad: Vector de capacidades (3,)
        
    Retorna:
        pd.DataFrame con el registro de métricas diarias acumuladas.
    """
    num_dias, consultas_por_dia = matriz_entrada.shape
    registros = []
    costo_acumulado = 0.0

    for d in range(num_dias):
        t_in = matriz_entrada[d]
        t_out = matriz_salida[d]
        
        asignacion = politica_asignacion(t_in)
        costos = calcular_costo(t_in, t_out, asignacion, precios)
        atencion = evaluar_atencion(t_in, asignacion, capacidad)
        
        costo_dia = float(np.sum(costos))
        costo_acumulado += costo_dia
        
        c_peq = int(np.sum(asignacion == 0))
        c_med = int(np.sum(asignacion == 1))
        c_gra = int(np.sum(asignacion == 2))
        
        costo_peq = float(np.sum(costos[asignacion == 0]))
        costo_med = float(np.sum(costos[asignacion == 1]))
        costo_gra = float(np.sum(costos[asignacion == 2]))
        
        registros.append({
            "dia": d + 1,
            "cantidad_consultas": len(t_in),
            "tokens_entrada_total": int(np.sum(t_in)),
            "tokens_salida_total": int(np.sum(t_out)),
            "costo_dia": round(costo_dia, 4),
            "costo_acumulado": round(costo_acumulado, 4),
            "consultas_bien_atendidas": int(np.sum(atencion)),
            "pct_bien_atendidas": round(float(np.mean(atencion) * 100), 2),
            "consultas_pequeno": c_peq,
            "consultas_mediano": c_med,
            "consultas_grande": c_gra,
            "costo_pequeno": round(costo_peq, 4),
            "costo_mediano": round(costo_med, 4),
            "costo_grande": round(costo_gra, 4),
        })

    return pd.DataFrame(registros)


def simular_con_presupuesto(
    matriz_entrada: np.ndarray,
    matriz_salida: np.ndarray,
    precios: np.ndarray,
    capacidad: np.ndarray,
    costo_referencia_p1: float,
    umbrales: list[int] = [200, 1000]
) -> tuple[pd.DataFrame, dict]:
    """
    Simulación con presupuesto mensual con tope al 60% del costo de Política 1.
    """
    presupuesto_limite = 0.60 * costo_referencia_p1
    num_dias = matriz_entrada.shape[0]
    
    registros = []
    costo_acumulado = 0.0
    presupuesto_agotado = False
    dia_agotado = None
    
    for d in range(num_dias):
        t_in = matriz_entrada[d]
        t_out = matriz_salida[d]
        
        if presupuesto_agotado:
            asignacion = np.full_like(t_in, 0, dtype=int)
        else:
            asignacion = asignar_modelo(t_in, umbrales)
            
        costos = calcular_costo(t_in, t_out, asignacion, precios)
        atencion = evaluar_atencion(t_in, asignacion, capacidad)
        
        costo_dia = float(np.sum(costos))
        costo_acumulado += costo_dia
        
        if not presupuesto_agotado and costo_acumulado >= presupuesto_limite:
            presupuesto_agotado = True
            dia_agotado = d + 1
            
        registros.append({
            "dia": d + 1,
            "costo_dia": round(costo_dia, 4),
            "costo_acumulado": round(costo_acumulado, 4),
            "presupuesto_agotado": presupuesto_agotado,
            "consultas_bien_atendidas": int(np.sum(atencion)),
            "total_consultas": len(t_in)
        })
        
    df_res = pd.DataFrame(registros)
    tot_consultas = df_res["total_consultas"].sum()
    pct_final = (df_res["consultas_bien_atendidas"].sum() / tot_consultas) * 100
    
    reporte = {
        "dia_agotado": dia_agotado,
        "costo_final": round(costo_acumulado, 4),
        "presupuesto_tope": round(presupuesto_limite, 4),
        "pct_bien_atendidas": round(pct_final, 2)
    }
    
    return df_res, reporte
