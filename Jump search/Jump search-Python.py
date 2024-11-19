import math

# Función para implementar el algoritmo Jump Search
def busquedaPorSaltos(arr, x, n):
    # Definir el tamaño del salto (raíz cuadrada del tamaño del arreglo)
    salto = math.sqrt(n)
    anterior = 0

    # Buscar el bloque donde puede estar el elemento
    while arr[int(min(salto, n) - 1)] < x:
        anterior = salto
        salto += math.sqrt(n)
        # Si hemos superado el tamaño del arreglo, el elemento no está presente
        if anterior >= n:
            return -1

    # Realizar una búsqueda lineal dentro del bloque identificado
    while arr[int(anterior)] < x:
        anterior += 1
        # Si alcanzamos el siguiente bloque o el final del arreglo, no está presente
        if anterior == min(salto, n):
            return -1

    # Comprobar si el elemento se encuentra en la posición actual
    if arr[int(anterior)] == x:
        return int(anterior)
    
    # Si no se encuentra, retornar -1
    return -1

# Datos de prueba
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55  # Elemento que queremos buscar
n = len(arr)  # Tamaño del arreglo

# Llamar a la función para buscar el índice del elemento
indice = busquedaPorSaltos(arr, x, n)

# Imprimir el resultado
print("El número", x, "se encuentra en el índice", indice)
