# Conjunto de funções que auxiliem no cálculo de matrizes e vetores


# Array MxN zerado
def zeroarray(m, n):
    return [[0 for j in range(n)] for i in range(m)]


# Multiplicação por Escalar
def escmult(array, escalar):

    if isinstance(array[0], list):
        m = len(array)
        n = len(array[0])
    
        return [[array[i][j]*escalar for j in range(n)] for i in range(m)]
    
    else:
        return [i * escalar for i in array]

# Multiplicação de Matrizes
def matmult(A, B):
    if isinstance(A[0], list) and isinstance(B[0], list):

        linhaA = len(A)
        colunaA = len(A[0])

        linhaB = len(B)
        colunaB = len(B[0])

        array = zeroarray(linhaA, colunaB)

        if colunaA == linhaB:
            for i in range(linhaA):
                for j in range(colunaB):
                    lista1 = A[i]
                    lista2 = [linha[j] for linha in B]

                    valores = [x * y for x, y in zip(lista1, lista2)]
                
                    array[i][j] = sum(valores)
        
            return array

        else:
            print("colA != rowB")
            return None

# ----------------------------------------------------------

    elif isinstance(B[0], int) or isinstance(B[0], float):
        
        linhaA = len(A)
        colunaA = len(A[0])

        linhaB = len(B)
        colunaB = 1

        array = zeroarray(linhaA, colunaB)

        if colunaA == linhaB:
            for i in range(linhaA):
                valores = [x * y for x,y in zip(A[i], B)]

                array[i] = sum(valores)

            return array

        else:
            print("colA != rowB")
            return None

