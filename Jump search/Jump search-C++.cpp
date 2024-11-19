// Programa en C++ para implementar Jump Search
 
#include <bits/stdc++.h>
using namespace std;
 
// Función para realizar Jump Search
int jumpSearch(int arr[], int x, int n)
{
    // Tamaño del bloque a saltar
    int paso = sqrt(n);
 
    // Buscar el bloque donde está el elemento
    int prev = 0;
    while (arr[min(paso, n) - 1] < x)
    {
        prev = paso;
        paso += sqrt(n);
        if (prev >= n)
            return -1; // Elemento no encontrado
    }
 
    // Búsqueda lineal dentro del bloque
    while (arr[prev] < x)
    {
        prev++;
        if (prev == min(paso, n))
            return -1; // Elemento no encontrado
    }

    // Retornar índice si se encuentra el elemento
    if (arr[prev] == x)
        return prev;
 
    return -1;
}
 
// Función principal para probar Jump Search
int main()
{
    int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 
                  34, 55, 89, 144, 233, 377, 610 };
    int x = 55;
    int n = sizeof(arr) / sizeof(arr[0]);
     
    // Buscar el índice de 'x' usando Jump Search
    int indice = jumpSearch(arr, x, n);
 
    // Imprimir el índice del elemento
    cout << "\nEl numero " << x << " este en el indice " << indice;
    return 0;
}

