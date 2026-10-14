from src_apoio.HelpMatriz import zeroarray, escmult, matmult
import math
import pyglet as pg
from pyglet.math import Mat4


# ----------------- Funções Complementares -------------------

def arestas(i, j, matriz):
    A = matriz[i]
    B = matriz[j]

    pg.shapes.Line(A[0] + 1920/2, A[1] + 1080/2, B[0] + 1920/2, B[1] + 1080/2, color = (255, 255, 255)).draw()

# ----------------- Formas --------------------

# Ângulos de rotação, um ângulo para eixo afim de evitar a fixação de pontos em torno do eixo de rotação final
thetax = 0.011
thetay = 0.015
thetaz = 0.02


# Raio dos pontos
raio = 7

# Criação dos pontos que formam a pirâmide base triangular
pontos = [
            [-200.0, -100.0, 75.0],
            [200.0, -100.0, 75.0],
            [0.0, -100.0, -125.0],
            [0.0, 300.0, -25.0]
        ]


# Matriz de Perspectiva
matriz_perspec = zeroarray(4,2)

# Matrizes de Rotação
rotXYZ = [
            [math.cos(thetay)*math.cos(thetaz), -math.cos(thetay)*math.sin(thetaz), math.sin(thetay)],
            [math.sin(thetax)*math.sin(thetay)*math.cos(thetaz) + math.cos(thetax)*math.sin(thetaz), -math.sin(thetax)*math.sin(thetay)*math.sin(thetaz) + math.cos(thetax)*math.cos(thetaz), -math.sin(thetax)*math.cos(thetay)],
            [-math.cos(thetax)*math.sin(thetay)*math.cos(thetaz) + math.sin(thetax)*math.sin(thetaz), math.cos(thetax)*math.sin(thetay)*math.sin(thetaz) + math.sin(thetax)*math.cos(thetaz), math.cos(thetax)*math.cos(thetay)]
        ] 

rotX = [
            [1, 0, 0],
            [0, math.cos(thetax), -math.sin(thetax)],
            [0, math.sin(thetax), math.cos(thetax)]
        ]

rotY = [
            [math.cos(thetay), 0, math.sin(thetay)],
            [0, 1, 0],
            [-math.sin(thetay), 0, math.cos(thetay)]
        ]

rotZ = [
            [math.cos(thetaz), -math.sin(thetaz), 0],
            [math.sin(thetaz), math.cos(thetaz), 0],
            [0, 0, 1]
        ]

# --------------------- Criação da Superfície -------------------

# Superfície
screen = pg.window.Window(fullscreen = True)


# Projetando e Renderizando na superfície
@screen.event
def on_draw():
    screen.clear()
    
    for ind in range(len(pontos)):

        # Rotacionando
        pontos[ind] = matmult(rotXYZ, pontos[ind])

        # Projeção em perspectiva
        z = 900 / (900 - pontos[ind][2])
        
        # Atualização de x e y a partir de "z" para projeção de profundidade
        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)

        # Renderizando cada ponto
        pg.shapes.Circle(x = matriz_perspec[ind][0] + 1920/2, y = matriz_perspec[ind][1] + 1080/2, radius = raio, color = (230,0,255)).draw()

    # Conectando vértices
    for i in range(3):
        arestas(i, (i+1)%3, matriz_perspec)
        arestas(i, 3, matriz_perspec)



pg.app.run()
