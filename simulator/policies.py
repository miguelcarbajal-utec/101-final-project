import numpy as np

def asignar_modelo(tokens_entrada: np.ndarray, umbrales: list[int] | np.ndarray) -> np.ndarray:
    """
    Asigna a cada consulta el índice del modelo correspondiente según su tamaño en tokens.
    
    0 (pequeno): si tokens < umbrales[0]
    1 (mediano): si umbrales[0] <= tokens < umbrales[1]
    2 (grande):  en cualquier otro caso (tokens >= umbrales[1])
    
    Retorna un arreglo de enteros del mismo tamaño que la entrada.
    """
    return np.digitize(tokens_entrada, bins=umbrales).astype(int)


def politica_todo_grande(tokens_entrada: np.ndarray) -> np.ndarray:
    """Política 2: Todas las consultas van al modelo grande (índice 2)."""
    return np.full_like(tokens_entrada, 2, dtype=int)


def politica_todo_pequeno(tokens_entrada: np.ndarray) -> np.ndarray:
    """Política 3: Todas las consultas van al modelo pequeño (índice 0)."""
    return np.full_like(tokens_entrada, 0, dtype=int)
