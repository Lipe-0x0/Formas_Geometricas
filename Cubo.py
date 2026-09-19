from src_apoio.HelpMatriz import zeroarray, escmult, matmult
import numpy as np
import pyglet as pg
from pyglet.math import Mat4


# ----------------- Funções Complementares -----------------

def arestas(i, j, Matriz):
    a = Matriz[i]
    b = Matriz[j]

    pg.shapes.Line(x = a[0], y = a[1], x2 = b[0], y2 = b[1], color = (255,255,255)).draw()

# ------------------ Formas ---------------------

# Ângulo de rotação
theta = 0.02

# Raio dos pontos
raio = 7

# Criação dos 4 pontos no espaço 2D
pontos = [
        [-100.0, -100.0, 100.0],
        [-100.0, 100.0, 100.0],
        [100.0, 100.0, 100.0],
        [100.0, -100.0, 100.0],
        [-100.0, -100.0, -100.0],
        [-100.0, 100.0, -100.0],
        [100.0, 100.0, -100.0],
        [100.0, -100.0, -100.0]
     ]

# Matriz de Perspectiva
matriz_perspec = zeroarray(8,2)


# Matrizes de rotação

rotZ = [
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0,0,1]
    ]
    

rotY = [
        [np.cos(theta), 0, -np.sin(theta)],
        [0,1,0],
        [np.sin(theta), 0, np.cos(theta)]
    ]


rotX = [
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0 ,np.sin(theta), np.cos(theta)]
    ]


# ------------------- Canva ---------------------

# Altura e Largura da Tela
alt = 750
lar = 750

# Superfície
screen = pg.window.Window(fullscreen = True)


# Redimensionando superfície para que centro seja (0,0)
@screen.event
def on_resize(width, height):
    # Projeção ortográfica 2D
    screen.projection = Mat4.orthogonal_projection(
            left = -width//2,
            right = width//2,
            bottom = -height//2,
            top = height//2,
            z_near = -255,
            z_far = 255
            )



@screen.event
def on_draw():
    screen.clear()

    for ind in range(len(pontos)):

        # Atualizando pontos ao aplicar as 3 rotações nele
        pontos[ind] = matmult(rotX, pontos[ind])

        # Perspectiva (Ideia geral = 1 / (distancia - z_original))
        z = 200 / (210 - pontos[ind][2])

        matriz_perspec[ind] = escmult(pontos[ind][0:2], z)
        
        # Desenhando pontos na tela
        pg.shapes.Circle(x = matriz_perspec[ind][0], y = matriz_perspec[ind][1], radius = raio, color = (230,0,255)).draw()

    # Desenhando arestas do Cubo
    for i in range(4):
        arestas(i, (i+1)%4, matriz_perspec)
        arestas(i+4, ((i+1)%4)+4, matriz_perspec)
        arestas(i, i+4, matriz_perspec)

pg.app.run()
