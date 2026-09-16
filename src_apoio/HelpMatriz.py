# Conjunto de funções que auxiliem no cálculo de matrizes e vetores


# Array MxN zerado
def zeroarray(m, n):
    array = [0 for [j for j in range(n)] in range(m)]

    print(array)


# Multiplicação por Escalar
def escmult(array, escalar):
    m = len(array)
    n = len(array[0])

    for i in range(m):
        for j in range(n):
            array[m,n] *= escalar

    return array


# Multiplicação de Matrizes
def matmul(A, B):
    linhaA = len(A)
    colunaA = len(A[0])

    linhaB = len(B)
    colunaB = len(B[0])

    if colunaA == linhaB:

    else:
        print("colA != rowB")
        return None
