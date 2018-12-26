import numpy as np


def main():
    #Crear Matriz NxM con numeros aleatorios
    Matriz = GenerarMatrizNumerosAleatorios(4, 8)

def GenerarMatrizNumerosAleatorios(N, M):
    if (N <= 2 or M <= 2):
        print('N y M deben ser mayores 2 ')
        return 0
    else:
        rand_matrix = np.random.randint(1,N*M + 1, (N, M))
        ContarColumnas(rand_matrix)

def ContarColumnas(matrix):

    totales = matrix.sum(axis=0)
    print('Suma Columnas', totales)

    even_columns = totales[1::2]
    media = even_columns.mean()
    print('Columnas Pares', even_columns)
    print('Promedio Totales Pares', even_columns.mean())

    nCols = Contar(totales, media)
    print('Numero de Columnas', nCols)

def Contar(totales, media):
    c = 0
    for val in totales:
        if (val > media):
            c += 1

    return c

if __name__ == '__main__':
  main()
