import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_dashboard(df_sim: pd.DataFrame, df_consultas_detalle: pd.DataFrame):
    """
    Genera la figura con los 5 gráficos obligatorios del Dashboard Final.
    """
    sns.set_theme(style="whitegrid", palette="muted")
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.35, wspace=0.25)
    
    # 1. Costo diario por modelo (Matplotlib)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(df_sim["dia"], df_sim["costo_pequeno"], label="Pequeño", marker="o", color="#2ecc71")
    ax1.plot(df_sim["dia"], df_sim["costo_mediano"], label="Mediano", marker="s", color="#f39c12")
    ax1.plot(df_sim["dia"], df_sim["costo_grande"], label="Grande", marker="^", color="#e74c3c")
    ax1.set_title("1. Costo Diario por Modelo (USD) [Matplotlib]", fontweight="bold")
    ax1.set_xlabel("Día")
    ax1.set_ylabel("Costo Diario (USD)")
    ax1.legend()
    
    # 2. Costo acumulado del mes (Matplotlib)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(df_sim["dia"], df_sim["costo_acumulado"], color="#2c3e50", linewidth=2.5)
    ax2.fill_between(df_sim["dia"], df_sim["costo_acumulado"], color="#34495e", alpha=0.15)
    ax2.set_title("2. Curva de Costo Acumulado del Mes (USD) [Matplotlib]", fontweight="bold")
    ax2.set_xlabel("Día")
    ax2.set_ylabel("Costo Acumulado (USD)")
    
    # 3. Distribución de tokens de entrada (Seaborn)
    ax3 = fig.add_subplot(gs[1, 0])
    sns.histplot(df_consultas_detalle["tokens_entrada"], kde=True, ax=ax3, color="#8e44ad", bins=40)
    ax3.set_title("3. Distribución de Tokens de Entrada por Consulta [Seaborn]", fontweight="bold")
    ax3.set_xlabel("Tokens de Entrada")
    ax3.set_ylabel("Frecuencia")
    
    # 4. Cantidad de consultas por modelo (Seaborn)
    ax4 = fig.add_subplot(gs[1, 1])
    conteo = [df_sim["consultas_pequeno"].sum(), df_sim["consultas_mediano"].sum(), df_sim["consultas_grande"].sum()]
    sns.barplot(x=["pequeno", "mediano", "grande"], y=conteo, ax=ax4, palette=["#2ecc71", "#f39c12", "#e74c3c"])
    ax4.set_title("4. Cantidad Total de Consultas por Modelo [Seaborn]", fontweight="bold")
    ax4.set_xlabel("Modelo")
    ax4.set_ylabel("Total Consultas")
    
    # 5. Heatmap de correlación (Seaborn)
    ax5 = fig.add_subplot(gs[2, :])
    corr = df_consultas_detalle[["tokens_entrada", "tokens_salida", "costo"]].corr()
    sns.heatmap(corr, annot=True, cmap="Blues", fmt=".3f", ax=ax5, vmin=0, vmax=1)
    ax5.set_title("5. Heatmap de Correlación: Tokens Entrada, Salida y Costo [Seaborn]", fontweight="bold")
    
    plt.tight_layout()
    return fig


def plot_comparativa_politicas(df_p1: pd.DataFrame, df_p2: pd.DataFrame, df_p3: pd.DataFrame):
    """
    Gráfico comparativo del costo acumulado a lo largo de los días para las tres políticas.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df_p1["dia"], df_p1["costo_acumulado"], label="Política 1 (Umbrales)", color="#2980b9", lw=2)
    plt.plot(df_p2["dia"], df_p2["costo_acumulado"], label="Política 2 (Todo Grande)", color="#c0392b", lw=2, linestyle="--")
    plt.plot(df_p3["dia"], df_p3["costo_acumulado"], label="Política 3 (Todo Pequeño)", color="#27ae60", lw=2, linestyle="-.")
    plt.title("Comparación de Costo Acumulado a 30 Días por Política de Asignación", fontweight="bold")
    plt.xlabel("Día")
    plt.ylabel("Costo Acumulado (USD)")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    return plt.gcf()
