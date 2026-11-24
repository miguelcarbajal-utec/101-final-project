# 💻 Simulador de Costos FinOps para Asistentes de IA

Proyecto final del curso **Programación 101 (Computación Científica en Python)** — Maestría en Ciencia de Datos e IA.

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
src_simulator/
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
└── tests/                   <- Pruebas unitarias de vectorización
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
