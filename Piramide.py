from src_apoio.HelpMatriz import zeroarray, escmult, matmult
import math
import pyglet as pg
from pyglet.math import Mat4


# ----------------- Funções Complementares -------------------

def arestas(i, j, matriz):
    A = matriz[i]
    B = matriz[j]

    pg.shapes.Line(A[0], A[1], B[0], B[1], color = (255, 255, 255)).draw()

# ----------------- Formas --------------------

# Ângulos de rotação, um ângulo para eixo afim de evitar a fixação de pontos em torno do eixo de rotação final
A = 0.011
B = 0.015
C = 0.02


# Raio dos pontos
raio = 7

# Criação dos pontos que formam a pirâmide base triangular
pontos = [
            [-200.0, -200.0, 100.0],
            [200.0, -200.0, 100.0],
            [0.0, -200.0, -100.0],
            [0.0, 200.0, 0.0]
        ]


# Matriz de Perspectiva
matriz_perspec = zeroarray(4,2)

# Matrizes de Rotação
rotXYZ = [
            [],
            [],
            []
        ] 

rotX = [
            [1, 0, 0],
            [0, math.cos(A), -math.sin(A)],
            [0, math.sin(A), math.cos(A)]
        ]

rotY = [
            [math.cos(B), 0, math.sin(B)],
            [0, 1, 0],
            [-math.sin(B), 0, math.cos(B)]
        ]

rotZ = [
            [math.cos(C), -math.sin(C), 0],
            [math.sin(C), math.cos(C), 0],
            [0, 0, 1]
        ]

# --------------------- Criação da Superfície -------------------

# Tamanho da tela (Largura x Altura)
lar = 720
alt = 720

# Superfície
screen = pg.window.Window(fullscreen = True)

# Redimensionando janela para que o centro seja (0,0)
@screen.event
def on_resize(width, height):
    # Projeção Ortográfica 2D
    screen.projection = Mat4.orthogonal_projection(
            left = -width/2,
            right = width/2,
            bottom = -height/2,
            top = height/2,
            z_near = -300,
            z_far = 300
            )

# Projetando e Renderizando na superfície
@screen.event
def on_draw():
    screen.clear()
    
    for ind in range(len(pontos)):

        # Rotacionando
        pontos[ind] = matmult(rotX, pontos[ind])
        pontos[ind] = matmult(rotY, pontos[ind])
        pontos[ind] = matmult(rotZ, pontos[ind])

        # Projeção em perspectiva
        z = 300 / (350 - pontos[ind][2])
        
        # Atualização de x e y a partir de "z" para projeção de profundidade
        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)

        # Renderizando cada ponto
        pg.shapes.Circle(x = matriz_perspec[ind][0], y = matriz_perspec[ind][1], radius = raio, color = (230,0,255)).draw()

    # Conectando vértices
    for i in range(3):
        arestas(i, (i+1)%3, matriz_perspec)
        arestas(i, 3, matriz_perspec)



pg.app.run()
