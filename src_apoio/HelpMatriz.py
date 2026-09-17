# Conjunto de funções que auxiliem no cálculo de matrizes e vetores


# Array MxN zerado
def zeroarray(m, n):
    return [[0 for j in range(n)] for i in range(m)]


# Multiplicação por Escalar
def escmult(array, escalar):
    m = len(array)
    n = len(array[0])
    
    return [[array[i][j]*escalar for j in range(n)] for i in range(m)]


# Multiplicação de Matrizes
def matmul(A, B):
    linhaA = len(A)
    colunaA = len(A[0])

    linhaB = len(B)
    colunaB = len(B[0])

    if colunaA == linhaB:
        print("awd")

    else:
        print("colA != rowB")
        return None
