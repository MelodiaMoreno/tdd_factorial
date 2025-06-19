"""Módulo para funciones matemáticas."""

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    n (int): Número entero no negativo.

    Retorna:
    int: Factorial de n.

    Excepciones:
    TypeError: Si n no es un entero.
    ValueError: Si n es negativo.
    """
    if not isinstance(n, int):
        raise TypeError("Debe introducirse un número entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n in (0, 1):
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
