# Conjunto de funções que auxiliem no cálculo de matrizes e vetores

# ----------- Função suporte ------------
def fatorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number*fatorial(number-1)
# ---------------------------------------

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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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


# Cálculo do cos/sen a partir da série de Taylor/Maclaurin(a = 0)

def seno(theta, n):
    radi_sen = 0
    for impar in range(n):
        radi_sen += (((-1)**impar / fatorial(2*impar + 1)) * theta**(2*impar + 1)) 

    return radi_sen

def cose(theta, n):
    radi_cos = 0
    for par in range(n):
        radi_cos += (((-1)**par / fatorial(2*par)) * theta**(2*par)) 
    
    return radi_cos
