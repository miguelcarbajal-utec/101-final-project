# 💻 Simulador de Costos FinOps para Asistentes de IA

Proyecto final del curso **Programación 101 (Computación Científica en Python)** — Maestría en Ciencia de Datos e IA.

---

## 🎯 Objetivo Educativo

Este proyecto aplica **computación científica vectorizada en Python** (operaciones matriciales con NumPy sin bucles a nivel de consulta) a un escenario práctico de **FinOps para asistentes de IA**. Permite modelar tráfico diario con distribución de colas pesadas (lognormal y datos reales de Dolly-15k) y analizar el compromiso (*trade-off*) entre **costo operativo (USD)** y **calidad de atención** al enrutar consultas entre tres tamaños de modelo (`pequeno`, `mediano`, `grande`) bajo distintas políticas y restricciones de presupuesto.

---

## ⚙️ ¿Qué es el Engine (`simulator/engine.py`)?

El módulo `engine.py` es el núcleo de simulación temporal del proyecto. Recorre la matriz mensual día por día (único bucle `for` permitido, manteniendo vectorizado todo el procesamiento diario de consultas) para orquestar el flujo completo:

- `ejecutar_simulacion()`: toma las matrices diarias de tokens de entrada y salida, aplica la política de asignación (`asignar_modelo` por umbrales, `politica_todo_grande` o `politica_todo_pequeno`), calcula costos y calidad de atención de forma vectorizada (`calcular_costo()` y `evaluar_atencion()`), y retorna un `DataFrame` con las métricas diarias y acumuladas del mes.
- `simular_con_presupuesto()`: simula un escenario con tope presupuestario mensual del **60%** respecto al costo de referencia de la Política 1; mientras hay saldo asigna por umbrales y, una vez agotado, degrada las consultas al modelo `pequeno` para medir el impacto en calidad y registrar el día exacto de agotamiento (`dia_agotado`).

---

## 🧰 Librerías Utilizadas

Según [`requirements.txt`](requirements.txt):

- **NumPy** (`>=1.24.0`): generación de tráfico lognormal, asignación vectorizada (`np.digitize`), *fancy indexing* sobre la matriz de tarifas y cálculo de costos y capacidades.
- **Pandas** (`>=2.0.0`): tabulación de resultados diarios/acumulados en `DataFrame`, lectura de JSONL/CSV y exportación de datasets procesados.
- **Matplotlib** (`>=3.7.0`) y **Seaborn** (`>=0.12.0`): visualización del dashboard de 5 gráficos y comparativa de políticas de costo acumulado.
- **Requests** (`>=2.28.0`): soporte para ingesta de datos externos desde el entorno.
- **Jupyter** (`>=1.0.0`): ejecución interactiva y documentación del análisis en el notebook entregable.
- **Pytest** (`>=7.0.0`): pruebas unitarias de generación, políticas, cálculo de costos y consistencia operativa.

---

## 🚀 Setup Rápido del Entorno de Desarrollo

Recomendado: Usar Python 3.10 o superior.

```bash
# 1. Crear entorno virtual
python3 -m venv .venv

# 2. Activar entorno virtual
# En macOS/Linux:
source .venv/bin/activate
# En Windows:
# .venv\Scripts\activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📂 Estructura del Código

```text
101-final-project/
├── data/
│   ├── raw/                 <- CSV de precios y consultas reales de Dolly-15k
│   └── processed/           <- Resultados de simulación exportados
├── simulator/               <- Módulos Python empaquetados
│   ├── config.py            <- Parámetros, matrices NumPy de precios y constantes
│   ├── generator.py         <- generar_consultas() y transformador de Dolly-15k
│   ├── policies.py          <- asignar_modelo() y políticas 1, 2, 3 + presupuesto
│   ├── metrics.py           <- calcular_costo() y evaluar_atencion()
│   ├── engine.py            <- ejecutar_simulacion() mensual
│   └── visualizer.py        <- Dashboard con Matplotlib y Seaborn
├── notebooks/
│   └── simulador_finops_ia.ipynb <- NOTEBOOK ENTREGABLE PARA EVALUACIÓN
├── tests/                   <- Pruebas unitarias de vectorización
├── pytest.ini               <- Configuración de rutas para pytest
└── requirements.txt         <- Dependencias del proyecto
```

---

## 🧪 Ejecutar Pruebas Unitarias
```bash
pytest tests/ -v
```

---

## 📓 Abrir el Notebook Entregable
```bash
jupyter lab notebooks/simulador_finops_ia.ipynb
```
