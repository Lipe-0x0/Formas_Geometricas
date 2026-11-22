import sys

# Definição do path(aŕea de trabalho) afim de localizar onde estão as funções do arquivo HelpMatriz.py
sys.path.insert(0, "/home/fan/Documentos/Python/PROJETOS PYTHON/Formas Geométricas")

from src_apoio.HelpMatriz import cose, seno, matmult, escmult, zeroarray
import pyglet as pg


# ------------------ Funções Complementares ------------------

def arestas(i, j, matriz):
    a = matriz[i]
    b = matriz[j]

    pg.shapes.Line(x = a[0] + 1920/2, y = a[1] + 1080/2, x2 = b[0] + 1920/2, y2 = b[1] + 1080/2, 
                   color = (255,255,255)).draw()


# ------------------ Formas -------------------

# Raio das bolas
raio = 7

# Ângulos para cada eixo de rotação(X, Y, Z)
thetax = 0.011
thetay = 0.015
thetaz = 0.02

# Determinando os 4 pontos que formarão a pirâmide com base triangular
pontos = [
            [-200.0, -100.0, 75.0, 0],
            [200.0, -100.0, 75.0, 0],
            [0, -100.0, -125.0, 0],
            [0, 300.0, -25.0, 1]
        ]


# Matriz de perspectiva
matriz_perspec = zeroarray(4, 4)


# Matrizes de Rotação
rotXYZ = [
            [cose(thetay, 100)*cose(thetaz, 100), -cose(thetay, 100)*seno(thetaz, 100), seno(thetay, 100), 0],
            [seno(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + cose(thetax, 100)*seno(thetaz, 100), -seno(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + cose(thetax, 100)*cose(thetaz, 100), -seno(thetax, 100)*cose(thetay, 100), 0],
            [-cose(thetax, 100)*seno(thetay, 100)*cose(thetaz, 100) + seno(thetax, 100)*seno(thetaz, 100), cose(thetax, 100)*seno(thetay, 100)*seno(thetaz, 100) + seno(thetax, 100)*cose(thetaz, 100), cose(thetax, 100)*cose(thetay, 100), 0],
            [0, 0, 0, 1]
        ]

rotZ = [
        [cose(thetaz, 100), -seno(thetaz, 100), 0],
        [seno(thetaz, 100), cose(thetaz, 100), 0],
        [0,0,1]
    ]


rotY = [
        [cose(thetay, 100), 0, seno(thetay, 100)],
        [0,1,0],
        [-seno(thetay, 100), 0, cose(thetay, 100)]
    ]


rotX = [
        [1, 0, 0],
        [0, cose(thetax, 100), -seno(thetax, 100)],
        [0 ,seno(thetax, 100), cose(thetax, 100)]
    ]

# Matriz de Projeção Perspectiva
# Onde n = near(próximo) e f = far(distante), d = distância do olho até o objeto
n = 900
# f = 300, como a terceira linha da multiplicação não é utilizada(até pq não estou fazendo um buffer) então achei melhor zerar
d = 900 # Critério de escolha: d > R, onde R é o maior môdulo dos vetores(vértices)

PP = [
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
    ]


# ---------------------- Canva ----------------------

# Superfície
screen = pg.window.Window(fullscreen = True)

@screen.event
def on_draw():
    screen.clear()


    for ind in range(len(pontos)):
        
        # Rotacionando pontos
        pontos[ind] = matmult(rotXYZ, pontos[ind])
        
        #
        matriz_perspec[ind] = matmult(PP, pontos[ind])
            
        #
        matriz_perspec[ind] = escmult(matriz_perspec[ind], 1/(d-matriz_perspec[ind][3]))


        pg.shapes.Circle(x = matriz_perspec[ind][0] + 1920/2, y = matriz_perspec[ind][1] + 1080/2, radius = raio,
                         color = (235,0,255)).draw()


    for i in range(3):
        arestas(i, (i+1)%3, matriz_perspec)
        arestas(i, 3, matriz_perspec)

pg.app.run()



